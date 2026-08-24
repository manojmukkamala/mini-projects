"""Investment simulation for the VFINX dashboard.

Compares how a hypothetical investor's money grows when saving 10% of the
US average wage and investing it in VFINX yearly, monthly, weekly, or daily,
or only on down days (dip buying).
The simulation runs from 1980 through end of 2019 (retirement) and assumes
tax-free (Roth-IRA style) returns.

Inputs  (CSV, in data/, produced by get_data.py):
  vfinx_df.csv, avg_wages.csv
Outputs (CSV, in data/):
  final_df.csv            Date, Close, Investment, Total_Shares,
                          Total_Investment, Investment_Value, Frequency
  timing_sim.csv          DCA timing simulation summary per strategy
  timing_sim_random.csv   1000 random-day draws of gain %

Usage:
  python get_data.py   # first
  python analyze.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"

SAVING_RATE = 0.10          # fraction of average wage invested
SIM_START = "1980-01-01"
SIM_END = "2019-12-31"      # hypothetical retirement at end of 2019

# DCA timing simulation (one unit bought per month)
TIMING_START = "1990-01-01"
TIMING_END = SIM_END
RANDOM_ITERATIONS = 1000
RNG_SEED = 42

# resample aliases for pandas >= 2.2 ('A'/'Y'/'M' were removed/renamed)
RESAMPLE_FREQ = {"Y": "YE", "M": "ME", "W": "W-MON", "D": "D"}

FREQUENCIES = [("Y", "Yearly"), ("M", "Monthly"), ("W", "Weekly"), ("D", "Daily")]


##########
# Loading & preparation
##########

def load_data():
    """Load extracted data produced by get_data.py; fetch it first if missing."""
    if not (DATA_DIR / "vfinx_df.csv").exists() or not (DATA_DIR / "avg_wages.csv").exists():
        import get_data
        get_data.main()
    vfinx_df = pd.read_csv(DATA_DIR / "vfinx_df.csv", parse_dates=["Date"])
    avg_wages = pd.read_csv(DATA_DIR / "avg_wages.csv", parse_dates=["Year"])
    return vfinx_df, avg_wages


def prepare_wages(avg_wages):
    """Ensure wages cover the simulation end year and add a Savings column.

    If the wage series ends before SIM_END, missing years are filled with
    the last known value (in 2020 the SSA series ended in 2018, so 2018
    wages were used as a proxy for 2019; the series now includes 2019+).
    """
    sim_end_year = pd.Timestamp(SIM_END).year
    if avg_wages["Year"].dt.year.max() < sim_end_year:
        missing = range(int(avg_wages["Year"].dt.year.max()) + 1, sim_end_year + 1)
        proxy = pd.DataFrame({
            "Year": [pd.Timestamp(f"{y}-01-01") for y in missing],
            "Avg_Wage": [float("nan")] * len(missing),
        })
        avg_wages = pd.concat([avg_wages, proxy], ignore_index=True)
    avg_wages = avg_wages.ffill()
    avg_wages["Savings"] = avg_wages["Avg_Wage"] * SAVING_RATE
    return avg_wages


##########
# Simulation
##########

def calc_returns(vfinx_df, avg_wages, freq="D", start_date=SIM_START, end_date=SIM_END):
    """Simulate investing the annual savings spread across periods of `freq`.

    Each period the investor buys (annual savings / days in that year)
    worth of fund shares at that period's last close. After `end_date` the
    investor has retired: no further investing, and the investment value is
    just the final share count carried forward with current prices.
    """
    stop_investing = pd.Timestamp(end_date) + pd.Timedelta(days=1)
    pre = vfinx_df[vfinx_df["Date"] < stop_investing]
    post = vfinx_df[vfinx_df["Date"] >= stop_investing]

    days_df = pd.DataFrame(pd.date_range(start_date, end_date, freq="D"), columns=["Date"])
    daily_df = pd.merge(days_df, pre, on="Date", how="left").ffill().bfill()
    fund_df = daily_df.set_index("Date").resample(RESAMPLE_FREQ[freq]).last().reset_index()

    fund_df["Year"] = fund_df["Date"].dt.year
    wage_df = avg_wages.assign(Year=avg_wages["Year"].dt.year)
    fund_df = pd.merge(fund_df, wage_df, on="Year", how="left").bfill()

    num_periods = fund_df.groupby("Year").size()
    fund_df["Num_Days"] = fund_df["Year"].map(num_periods)

    fund_df["Investment"] = fund_df["Savings"] / fund_df["Num_Days"]
    fund_df["Shares_Purchased"] = fund_df["Investment"] / fund_df["Close"]
    fund_df["Total_Shares"] = fund_df["Shares_Purchased"].cumsum()
    fund_df["Total_Investment"] = fund_df["Investment"].cumsum()

    fund_df = pd.merge(daily_df, fund_df.drop("Close", axis=1), on="Date", how="left").ffill().fillna(0)

    # Extend past the simulation end so the chart spans the full price history
    fund_df = pd.concat([fund_df, post])[["Date", "Close", "Investment", "Total_Shares", "Total_Investment"]].ffill()

    fund_df["Investment_Value"] = fund_df["Total_Shares"] * fund_df["Close"]

    return fund_df


def calc_dip_returns(vfinx_df, avg_wages, start_date=SIM_START, end_date=SIM_END):
    """Dip-buying variant: invest each year's savings only on down-close days.

    Same economics as calc_returns(freq="D"), but nothing is bought on up
days; the annual savings is spread evenly over that year's down days.
    """
    stop_investing = pd.Timestamp(end_date) + pd.Timedelta(days=1)
    pre = vfinx_df[vfinx_df["Date"] < stop_investing]
    post = vfinx_df[vfinx_df["Date"] >= stop_investing]

    days_df = pd.DataFrame(pd.date_range(start_date, end_date, freq="D"), columns=["Date"])
    daily = pd.merge(days_df, pre, on="Date", how="left").ffill().bfill()

    down = daily["Close"].diff() < 0
    down_days = daily.assign(Down=down).groupby(daily["Date"].dt.year)["Down"].transform("sum")

    daily["Year"] = daily["Date"].dt.year
    wage_df = avg_wages.assign(Year=avg_wages["Year"].dt.year)
    daily = pd.merge(daily, wage_df, on="Year", how="left").bfill()

    daily["Investment"] = (daily["Savings"] / down_days).where(down, 0.0)
    daily["Shares_Purchased"] = daily["Investment"] / daily["Close"]
    daily["Total_Shares"] = daily["Shares_Purchased"].cumsum()
    daily["Total_Investment"] = daily["Investment"].cumsum()

    out = daily[["Date", "Close", "Investment", "Total_Shares", "Total_Investment"]]
    tail = post[["Date", "Close"]].copy()
    tail["Investment"] = 0.0
    tail["Total_Shares"] = out["Total_Shares"].iloc[-1]
    tail["Total_Investment"] = out["Total_Investment"].iloc[-1]

    out = pd.concat([out, tail], ignore_index=True)
    out["Investment_Value"] = out["Total_Shares"] * out["Close"]
    return out


##########
# DCA timing simulation
##########

def _score_purchases(prices, latest_price):
    """Score one unit bought per month at `prices`; return (invested, value, gain %)."""
    prices = np.asarray(prices, dtype=float)
    invested = prices.sum()
    final_value = latest_price * len(prices)
    gain_percent = (final_value - invested) / invested * 100
    return invested, final_value, round(gain_percent, 2)


def timing_simulation(vfinx_df):
    """Simulate how the purchase day within each month changes DCA outcomes.

    One unit of VFINX is bought every month from TIMING_START to TIMING_END;
    strategies differ only in which day of the month they buy on:
      Lucky    - the month's lowest price (unachievable in practice)
      Unlucky  - the month's highest price (unachievable in practice)
      First    - the first trading day of the month
      Random   - a random trading day of the month (seeded)
      Analyst  - the calendar day that most often recorded the monthly low
                 in all prior history for that month (backs up to the last
                 trading day if it falls on a non-trading day)

    Returns (summary, random_gains) and writes both to CSV.
    """
    df = vfinx_df[["Date", "Close"]].set_index("Date").sort_index()
    sim = df[(df.index >= TIMING_START) & (df.index <= TIMING_END)]
    history = df[df.index < TIMING_START]
    latest_price = sim["Close"].iloc[-1]

    day_map = {k: g.index for k, g in sim.groupby([sim.index.year, sim.index.month])}

    # Analyst: walk the months, tracking the most common monthly-low day
    # per calendar month over all history seen so far.
    hist = history.copy()
    hist["Month"] = hist.index.month
    hist["Day"] = hist.index.day
    analyst_prices = []
    for (y, m) in sorted(day_map):
        past = hist[hist["Month"] == m]
        lows = past.loc[past.groupby(past.index.year)["Close"].idxmin()]
        best_day = int(lows["Day"].value_counts().idxmax())
        trading_days = day_map[(y, m)]
        prior = trading_days[trading_days.day <= best_day]
        purch_date = prior.max() if len(prior) else trading_days.min()
        analyst_prices.append(sim.loc[purch_date, "Close"])
        month_rows = sim.loc[trading_days].copy()   # history grows as in the original
        month_rows["Month"] = m
        month_rows["Day"] = month_rows.index.day
        hist = pd.concat([hist, month_rows])

    rng = np.random.default_rng(RNG_SEED)
    random_prices = [
        sim.loc[tdays[rng.integers(len(tdays))], "Close"] for tdays in (day_map[k] for k in sorted(day_map))
    ]

    strategies = {
        "Lucky": sim.resample("ME").min()["Close"],
        "Unlucky": sim.resample("ME").max()["Close"],
        "First": sim.resample("ME").first()["Close"],
        "Random": random_prices,
        "Analyst": analyst_prices,
    }
    rows = []
    for name, prices in strategies.items():
        invested, final_value, gain = _score_purchases(prices, latest_price)
        rows.append({
            "Strategy": name,
            "Total_Invested": round(invested, 2),
            "Final_Value": round(final_value, 2),
            "Gain_Percent": gain,
        })
    summary = pd.DataFrame(rows)

    # Distribution of gains across many random-day choices
    month_arrays = {k: sim["Close"].loc[tdays].to_numpy() for k, tdays in day_map.items()}
    keys = sorted(day_map)
    gains = []
    for _ in range(RANDOM_ITERATIONS):
        total = sum(arr[rng.integers(len(arr))] for arr in (month_arrays[k] for k in keys))
        gains.append(round((latest_price * len(keys) - total) / total * 100, 2))
    random_gains = pd.DataFrame({"Gain_Percent": gains})

    out1 = DATA_DIR / "timing_sim.csv"
    out2 = DATA_DIR / "timing_sim_random.csv"
    summary.to_csv(out1, index=False)
    random_gains.to_csv(out2, index=False)
    print(f"Saved timing simulation -> {out1}, {out2}")
    return summary, random_gains


##########
# Main
##########

def main():
    vfinx_df, avg_wages = load_data()
    avg_wages = prepare_wages(avg_wages)

    parts = []
    for freq, label in FREQUENCIES:
        df = calc_returns(vfinx_df, avg_wages, freq=freq)
        df["Frequency"] = label
        parts.append(df)

    dip_df = calc_dip_returns(vfinx_df, avg_wages)
    dip_df["Frequency"] = "Dip"
    parts.append(dip_df)

    final_df = pd.concat(parts, ignore_index=True)
    out = DATA_DIR / "final_df.csv"
    final_df.to_csv(out, index=False)
    print(f"Saved {len(final_df)} rows -> {out}")

    timing_simulation(vfinx_df)


if __name__ == "__main__":
    main()
