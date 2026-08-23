# Diabetic-Patients-Readmission-Prediction

In this project, I have analyzed the relationship between diabetes patient readmission and the various patient attributes.
The dataset was obtained from one of our professors at Northern Illinois University who is working on Statistical Modeling.

Performed initial data exploration and data cleansing using Excel (Pivot tables, Slicer and other advanced Excel functions).
The cleansed data file can be found in this repository named med_data.csv

## How to run

Requires R and the `ROCR` package (`install.packages("ROCR")`).
Run from this folder so that `med_data.csv` is found on disk:

```sh
Rscript Project_V4.R
```

The script prints the logistic-regression summary, odds ratios and confidence
intervals, then test-set accuracy, and plots the ROC curve with AUC.

##### Project_V4.R 

Holds the R code used to perform data analysis, data type conversions, data transformations etc.

Splitted the data into training and test sets and declared the reference value for categorical variables.

Using the training set, a sample was picked and logistic regression model was implemented.

Using the test set, predictions were made. Computed the accuracy of the model and built ROC curve.

---

*Original work: 2017-11 (first committed to GitHub 2017-11-07).*
