# death_rates

Multivariate linear regression on US state death rates, written in
MATLAB (coursework). The model predicts the death rate (column 17)
from 15 feature columns (population, temperatures, pollution, etc.)
using gradient descent, with a 75/25 train/test split.

## How to run

Requires MATLAB (or GNU Octave). From this directory:

1. Load the dataset into the workspace as `DeathRateLinearRegdataset`
   (e.g. `DeathRateLinearRegdataset = csvread('Death Rate - Linear Reg dataset.csv');`).
2. Run `DeathRates_LinearReg.m` — it normalizes the features, splits
   the data, runs gradient descent, plots the cost history, and
   reports predictions on the test set.

Supporting functions: `computeCostMulti.m`, `featureNormalize.m`,
`gradientDescentMulti.m`, `normalEqn.m`.

## Notes

For this exercise, I have used the data from:
http://people.sc.fsu.edu/~jburkardt/datasets/regression/x28.txt

There are 60 rows and 17 columns.

This is the data regarding the death rates as a function of other
variables like Population, Temperatures etc.

I have split the data for train and test purposes (75% and 25%). I
have used the Gradient descent algorithm to find the parameters.

Cost varies over a range of 200-300 with every trial due to the random
number generator I've used to pick the training set.

I found that the relative pollution potential of oxides of Nitrogen has
a great effect on death rates followed by the size of the nonwhite
population. Death rate increases with nitric oxide pollution.

DeathRates_LinearReg.m is the file where I placed the code.
