x <- read.table("med_data.csv", header = TRUE, sep=",")

#I have changed these columns to factors instead of factors.
#Converting Some Quantitative variables to factors as well as they are Nominal data type
x$admission_type_id <- factor(x$admission_type_id)
x$discharge_disposition_id <- factor(x$discharge_disposition_id)
x$admission_source_id <- factor(x$admission_source_id)
x$A1Cresult <- factor(x$A1Cresult)

#Converting the remaining quantitaive variables to numeric
#Number of days between admission and discharge
x$time_in_hospital <- as.numeric(x$time_in_hospital)

#Number of lab tests performed during the encounter
x$num_lab_procedures <- as.numeric(x$num_lab_procedures)

#Number of procedures (other than lab tests) performed during the encounter
x$num_procedures <- as.numeric(x$num_procedures)

#Number of distinct generic names administered during the encounter
x$num_medications <- as.numeric(x$num_medications)

#Number of distinct generic names administered during the encounter
x$number_diagnoses <- as.numeric(x$number_diagnoses)


#Converting Qualitative data to Factor
x$race <- factor(x$race)
x$gender <- factor(x$gender)
x$metformin <- factor(x$metformin)
x$glipizide <- factor(x$glipizide)
x$glyburide <- factor(x$glyburide)
x$insulin <- factor(x$insulin)
x$change <- factor(x$change)
x$diabetesMed <- factor(x$diabetesMed)

#Converting Age to Numeric for the sake of easy application on model.
# A value of 1 in Age means (0 - 10), 2 means (10 20) ..etc
x$age <- as.numeric(x$age)
x$age <- as.factor(x$age)

#Certain Records in Race are NULL. Let's get rid of them.
y <- subset(x, !(x$race %in% "?"))

#Working on Output variable

#Converting it to character for the sake of converting it to 0's and 1's
y$readmitted <- as.character(y$readmitted)

for (i in 1:length(y$readmitted))
{
  if (y$readmitted[i] %in% "NO")
  {
    y$readmitted[i] = "0"
  }
  else
  {
    y$readmitted[i] = "1"
  } 
}

#Converting it back to Numeric
y$readmitted <- as.numeric(y$readmitted)

#I believe these columns dont have anything to do with the output as they seem some sort of randomly generated values. Let's ignore them and we will look into them later.
#Cutting off diag_1, diag_2, diag_3
z <- subset(y, select = -c(diag_1, diag_2, diag_3))


#Creating Training & Test sets
r <- sample(2, nrow(z), replace = T, prob = c(0.75, 0.25))
trainset <- z[r == 1, 1:19]
testset <- z[r == 2, 1:19]

#In Regression, if you have columns with levels in data, we can set a reference level. If we do not set any reference level, the first level in the column will be taken as reference level.
#Setting reference levels to certain variables
trainset$A1Cresult <- relevel(as.factor(trainset$A1Cresult), "None")
trainset$insulin <- relevel(as.factor(trainset$insulin), "No")
trainset$glyburide <- relevel(as.factor(trainset$glyburide), "No")
trainset$glipizide <- relevel(as.factor(trainset$glipizide), "No")
trainset$metformin <- relevel(as.factor(trainset$metformin), "No")
trainset$change <- relevel(as.factor(trainset$change), "No")

#Reducing the Sets
trainset <- trainset[1:7500, ]
testset <- testset[1:2500, ]

#Just writing the names of all the variables under one term to avoid re-writing when we apply model multiple times
drivers <- c("race", "gender", "age", "admission_type_id", "discharge_disposition_id", "admission_source_id", "time_in_hospital", "num_lab_procedures", "num_procedures", "num_medications", "number_diagnoses", "A1Cresult", "metformin", "glipizide", "glyburide", "insulin", "change", "diabetesMed")

#Writing the name of dependent variable seperately
dependentVar <- "readmitted"

#Bringing all the column names under one term
m <- paste(dependentVar, "~", paste(drivers, collapse = " + "))
m

#Logistic Regression
mylogit <- glm(m, data = trainset, family = binomial(link = "logit"), na.action = na.pass)
summary(mylogit)
exp(mylogit$coefficients)
confint(mylogit)

#Pseudo-R square
1 - with(mylogit, deviance/null.deviance)

#Test set prediction
predTest <- predict(mylogit, testset[,1:18], type = "response")
thres <- 0.5
predFac <- cut(predTest, breaks = c(-Inf, thres, Inf), labels = c("0", "1"))
cTab <- table(testset$readmitted, predFac, dnn = c("actual", "predicted"))
addmargins(cTab)

#Calculating Accuracy
accuracy <- sum(diag(cTab))/sum(cTab)
accuracy

#Probability scores on training data & ROC Curve
pred <- predict(mylogit, type = "response")
predObj <- prediction(pred, trainset$readmitted)
rocObj <- performance(predObj, measure = "tpr", x.measure = "fpr")
aucObj <- performance(predObj, measure = "auc")
auc = aucObj@y.values[[1]]
auc
plot(rocObj, main = paste("Area under the curve: ", auc))
