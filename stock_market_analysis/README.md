# stock_market_analysis

Stock-market analysis projects: two standalone analysis notebooks plus a
VFINX ROI-simulation subproject.

## Contents

| Item | What it is |
|---|---|
| `nifty_bank_analysis.ipynb` | Weekly momentum study of the NSE Bank Index (`^NSEBANK`): Monday-open → Friday-close spread, z-score bands, 3-week rolling signal. Fetches data from Yahoo Finance at runtime. |
| `sp500_sectors_analysis.ipynb` | S&P 500 sector weights + a "factor" ranking (weight combined with one-year growth). Scrapes the constituent list from Wikipedia and slickcharts, prices from Yahoo Finance, at runtime. |
| `roi_simulation/` | VFINX (Vanguard 500 Index Fund) ROI simulation + Streamlit dashboard — invest 10% of the US average wage yearly/monthly/weekly/daily, 1980–2019, plus a DCA timing study. See its README. |

## Notes

- The notebooks are self-contained (they fetch their own data at
  runtime); no data files ship with them.
- `roi_simulation` commits the two small input CSVs (public sources:
  Yahoo Finance, SSA) and regenerates its derived outputs locally.
