# melbourne_housing

Intro-to-machine-learning tutorial on the Kaggle **Melbourne Housing**
dataset: predict house sale prices with a decision tree, tune it, and
compare against a random forest. Written in Colab, June 2020 (the
notebook's own title: "Intro to Machine Learing" [sic]).

`MachineLearningKaggle.ipynb` walks through, in order:

1. Load `melb_data.csv`, `describe()`, drop rows with missing values.
2. Target `Price`; feature set 1 = Rooms, Bathroom, Landsize,
   Lattitude, Longtitude → fit `DecisionTreeRegressor(random_state=1)`,
   sanity-check predictions on 5 houses.
3. Feature set 2 adds BuildingArea and YearBuilt; refit, compute MAE
   on the full data, then do a proper `train_test_split`
   (`random_state=0`) and report validation MAE.
4. Hyperparameter search: `get_mae()` over `max_leaf_nodes` ∈
   {5, 50, 500, 5000}.
5. `RandomForestRegressor(random_state=1)` baseline — validation MAE
   (lands below the tuned single-tree MAE).

Expected validation MAE, from the notebook's last Colab run: full-data
MAE 434,716; single unsplit tree 270,971; tuned tree best at
`max_leaf_nodes=500` → 243,495; random forest 191,670.

The last cells are empty scratch cells.

## How to run

```sh
pip install jupyter pandas scikit-learn
jupyter notebook MachineLearningKaggle.ipynb
```

Notebook ships with no outputs; run the cells in order.

## Notes

- **Stale path:** the first data cell loads from a Colab path
  (`/content/drive/My Drive/Colab Notebooks/melb_data.csv`). To run
  locally, change it to `pd.read_csv('melb_data.csv')` — the CSV sits
  next to the notebook.
- **Data:** `melb_data.csv` (13,580 rows × 21 columns) is the public
  Kaggle "House Prices in Melbourne" dataset, used by the Kaggle Learn
  *Intro to Machine Learning* course. A copy is committed here, so no
  download is needed; the original requires a Kaggle login —
  <https://www.kaggle.com/competitions/house-prices-in-melbourne/data>.
