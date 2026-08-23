# time_series_analysis

Practice notebook ("TSA") on the classic **Airline Passengers** time
series (monthly passenger counts, 1949–1960, 144 rows — the standard
Box & Jenkins example, included as `tsa.csv`), plus a small deep
learning experiment. Written in Colab, June–July 2020.

`TSA.ipynb` has three sections:

- **Prep** — warm-up exercises: `datetime` objects, numpy basics, a
  tour of pandas plotting (bar, line, area, scatter, box, kde, hexbin).
- **TSA** — the core analysis: load the CSV, set a monthly (`MS`)
  DatetimeIndex, compute the overall average plus 6- and 12-month
  moving averages (SMA), and plot them against the raw series. Also
  contains two half-baked scratch snippets (an sklearn
  `cross_val_score` block referencing undefined variables, and an
  `XGBRegressor` snippet with the train/test split commented out).
- **DNN** — fit a small Keras MLP (Dense 4 → 4 → 1, adam, MSE,
  300 epochs) to a synthetic noisy line `y = 2x + 3 + noise`, then
  plot the fit and the loss curve.

## How to run

```sh
pip install jupyter pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow
jupyter notebook TSA.ipynb
```

Notebook has no outputs stored; run the cells in order.

## Notes

- **Stale path:** the TSA section loads the CSV from a Colab path
  (`/content/drive/My Drive/Colab Notebooks/tsa.csv`). To run locally,
  change that cell to `pd.read_csv('tsa.csv')` (or point it at the
  CSV sitting next to the notebook).
- **Prep section** uses `np.random.seed(42)` for reproducibility of the
  plotting demos; the TSA/DNN sections do not seed their synthetic
  noise, so their exact plots vary per run.
- `tsa.csv` is the public airline-passengers dataset (Box & Jenkins,
  *Time Series Analysis*); a copy is committed here, so no download is
  needed.
