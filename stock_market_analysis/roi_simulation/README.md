# ROI Simulation

Simulates investing 10% of the US average wage into VFINX (Vanguard 500 Index Fund) yearly, monthly, or daily from 1980 to 2019, and visualizes the results in a Streamlit dashboard.

## Pipeline

| File | Purpose |
|---|---|
| `get_data.py` | Fetch VFINX prices (Yahoo Finance) + US average wages (SSA) into `data/` as CSV |
| `analyze.py` | Run the investment simulation + DCA timing simulation, writes `data/final_df.csv`, `data/timing_sim.csv`, `data/timing_sim_random.csv` |
| `app.py` | Streamlit dashboard |

Run (in order):

```bash
python get_data.py
python analyze.py
streamlit run app.py   # http://localhost:8501
```

`data/` holds the CSVs produced by the pipeline. The two input CSVs
(`vfinx_df.csv`, `avg_wages.csv`) are committed; the derived outputs
(`final_df.csv` — 8 MB —, `timing_sim.csv`, `timing_sim_random.csv`) are
gitignored and regenerated deterministically (seed 42) by `analyze.py`.
