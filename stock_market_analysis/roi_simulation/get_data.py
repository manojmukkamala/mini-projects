"""Data extraction: VFINX prices + US average wages.

Scope: fetching raw data only (no analysis).

Sources:
  - VFINX (Vanguard 500 Index Fund) daily prices: Yahoo Finance (yfinance)
  - US national average wage index: https://www.ssa.gov/oact/COLA/AWI.html

Outputs (CSV, in data/):
  vfinx_df.csv   Date, Close
  avg_wages.csv  Year, Avg_Wage

Usage:
  python get_data.py
"""

from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup
from curl_cffi import requests

DATA_DIR = Path(__file__).resolve().parent / "data"

TICKER = "VFINX"
START_DATE = "1980-01-01"
WAGE_URL = "https://www.ssa.gov/oact/COLA/AWI.html"
WAGE_START_YEAR = "1980"


##########
# VFINX prices
##########

def fetch_vfinx(ticker=TICKER, start_date=START_DATE, end_date=None):
    """Download daily fund prices. Returns a DataFrame with [Date, Close]."""
    if end_date is None:
        end_date = date.today()

    df = yf.download(ticker, start=start_date, end=end_date, progress=False, auto_adjust=False)
    if df.empty:
        raise RuntimeError(f"No data returned for {ticker}")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df.reset_index()
    df["Date"] = pd.to_datetime(df["Date"])
    return df[["Date", "Close"]]


##########
# US average wages
##########

def fetch_avg_wages():
    """Scrape the national average wage indexing series from SSA.

    Returns a DataFrame with [Year, Avg_Wage] from WAGE_START_YEAR onwards.
    """
    # SSA's WAF blocks non-browser TLS fingerprints, so use curl_cffi impersonation
    page = requests.get(WAGE_URL, impersonate="chrome", timeout=30).text
    soup = BeautifulSoup(page, "html.parser")

    # The last 3 tables on the page are the wage series
    # (1951-1980, 1981-2010, 2011-present), each with Year/Index columns.
    rows = []
    for table in soup.find_all("table")[-3:]:
        for row in table.find_all("tr"):
            columns = row.find_all("td")
            if columns:
                rows.append([column.get_text() for column in columns])

    avg_wages = pd.DataFrame(rows, columns=["Year", "Avg_Wage"])
    avg_wages["Year"] = pd.to_datetime(avg_wages["Year"])
    avg_wages["Avg_Wage"] = avg_wages["Avg_Wage"].apply(lambda x: x.replace(",", "")).astype(float)

    return avg_wages[avg_wages["Year"] >= WAGE_START_YEAR].reset_index(drop=True)


##########
# Main
##########

def main():
    DATA_DIR.mkdir(exist_ok=True)

    vfinx_df = fetch_vfinx()
    out = DATA_DIR / "vfinx_df.csv"
    vfinx_df.to_csv(out, index=False)
    print(f"Saved {len(vfinx_df)} rows "
          f"({vfinx_df['Date'].min().date()} to {vfinx_df['Date'].max().date()}) -> {out}")

    avg_wages = fetch_avg_wages()
    out = DATA_DIR / "avg_wages.csv"
    avg_wages.to_csv(out, index=False)
    print(f"Saved {len(avg_wages)} rows "
          f"({avg_wages['Year'].min().year} to {avg_wages['Year'].max().year}) -> {out}")


if __name__ == "__main__":
    main()
