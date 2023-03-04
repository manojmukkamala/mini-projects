# Installing all the required package for downstream analysis
install.packages(c("ggplot", "e1071", "caret", "quanteda", "irlba", "randomForest"))

# Reading in the dataset and viewsing the data
rawdata <- read.csv('spam.csv', stringsAsFactors = F, fileEncoding = 'UTF-16')
View(rawdata)

# Cleaning the dataframe, retaining only the required fields and re-naming them as 'Label'  and 'Text'.
rawdata <- rawdata[,1:2]
names(rawdata) <- c('Label', 'Text')
View(rawdata)

# Checking the dataframe for missing values
length(which(!complete.cases(rawdata)))

# Converting Class Label into Factor
rawdata$Label <- as.factor(rawdata$Label)

# Exploring the data
# Looking at the distribution of class Labels
table(rawdata$Label)
prop.table(table(rawdata$Label))

# Getting the distribution of text length of the input text messagesby adding a new feature to the data frame
rawdata$TextLength <- nchar(rawdata$Text)
summary(rawdata$TextLength)

#Visualising the distribution of Text Length identified with class label 
library(ggplot2)

ggplot() +
  theme_bw() +
  geom_histogram(data = rawdata, aes(x = TextLength, fill = Label), binwidth = 5) +
  labs(y = "Text Count", x = "Length of Text",
       title = "Distribution of Text Lengths with Class Labels")
