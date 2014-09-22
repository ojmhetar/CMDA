setwd("C:/Users/ojmhetar/Downloads")

load("exampleData1.rData")
?merge
norm.income <- merge(custdata, medianincome)

summary(norm.income)

#Normalization makes sense when you want to compare the average income
#of an individual relative to the location where he lives, not to the
#national average or average of another state.

norm.income$gp <- runif(dim(norm.income)[1])

testSet <- subset(norm.income, norm.income$gp <= .7)

trainingSet <- subset(norm.income, norm.income$gp > .7)

dim(testSet)[1]
dim(trainingSet)[1]
