# text_analytics

Spam/ham SMS classification (and a look at topic modelling), written
in R (coursework). Built using the SMS Spam Collection dataset from
Kaggle/UCI, following the Data Science Dojo text-analytics YouTube
tutorials.

## How to run

Requires R. From this directory:

```r
install.packages(c("ggplot", "e1071", "caret", "quanteda", "irlba", "randomForest"))
source('Code1.R')
```

Note: `spam.csv` is UTF-16 encoded; the script reads it with
`fileEncoding = 'UTF-16'`.

## Data

`spam.csv` — SMS Spam Collection dataset
(https://www.kaggle.com/uciml/sms-spam-collection-dataset).

## Credits

Tutorials: https://www.youtube.com/playlist?list=PL8eNk_zTBST8olxIRFoo0YeXxEOkYdoxi
