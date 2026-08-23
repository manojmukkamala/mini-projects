# ionosphere

Classification study on the UCI **Johns Hopkins University Ionosphere**
dataset: 351 radar-return instances × 34 numeric features, labeled
`g` (good) / `b` (bad), from Sigillito et al. (1989), *Classification
of radar returns from the ionosphere using neural networks*, Johns
Hopkins APL Technical Digest 10, 262–266 (the original work got ~96 %
accuracy with backprop).

`IonosphereModel.ipynb` (48 cells) does, in order:

1. Load the data — from the UCI URL at runtime (a local copy is also
   committed, see below).
2. Name the 34 feature columns (`col_1`…`col_34`) + `target`, encode
   `g`/`b` → 1/0, and drop `col_2` (constant zero).
3. Base models: K-fold (`k` = 2…10) train/test error and accuracy
   curves for `LogisticRegression` and `DecisionTreeClassifier`.
4. Bagging: `BaggingClassifier` around both bases, varying `k` with
   fixed ensembles, then fixed `k=7` with varying ensemble size.
5. Boosting: same two sweeps with `AdaBoostClassifier`.

## Files

- `ionosphere.data` (76,467 B) — the dataset, byte-for-byte the UCI
  file.
- `ionosphere.names` (3,116 B) — UCI attribute/donor documentation.
- `Index` — the UCI directory listing the download came from.
- `IonosphereModel.ipynb` — the study (no stored outputs).

## How to run

```sh
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
jupyter notebook IonosphereModel.ipynb
```

Run the cells in order; the model sweeps take a few minutes.

## Data

The notebook fetches the data at runtime from the UCI Machine Learning
Repository (URL verified live 2026-08-23, matching the committed
copy):

```
https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data
https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.names
```

If the URL ever moves, the committed `ionosphere.data` works as-is —
point the first data cell at it with
`pd.read_csv('ionosphere.data', header=None)`.
