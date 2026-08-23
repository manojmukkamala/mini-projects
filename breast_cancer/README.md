# breast_cancer

Logistic-regression classifier for the UCI Wisconsin breast-cancer
dataset, written in MATLAB (coursework). Binary logistic regression is
trained on the 30 `*_mean` features to classify tumors as malignant (1)
or benign (0), using two fitting approaches:

- `cancer_gradientdescent.m` — batch gradient descent (expected
  training accuracy ≈ 98.5 %)
- `cancer_fminunc.m` — fits theta with MATLAB's `fminunc`
  (expected training accuracy ≈ 98.7 %)

## How to run

Requires MATLAB (or GNU Octave). From this directory:

1. Load the dataset into the workspace as `Cancerdata`
   (label in column 1, features in columns 2:31):

   ```matlab
   Cancerdata = csvread('Cancer_data.csv');
   ```

2. Run either `cancer_gradientdescent.m` or `cancer_fminunc.m`.

Supporting functions: `costFunction.m`, `featureNormalize.m`,
`gradientDescentMulti.m`, `predict.m`, `sigmoid.m`.

## Data

`Cancer_data.csv` — 569 samples × 31 columns (diagnosis label + 30
features), from the UCI Machine Learning Repository.

Data Set Information:

Features are computed from a digitized image of a fine needle aspirate
(FNA) of a breast mass. They describe characteristics of the cell
nuclei present in the image.

Citation:
Lichman, M. (2013). UCI Machine Learning Repository
[http://archive.ics.uci.edu/ml]. Irvine, CA: University of California,
School of Information and Computer Science.

Here is a BiBTeX citation as well:

```bibtex
@misc{Lichman:2013 ,
author = "M. Lichman",
year = "2013",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences" }
```
