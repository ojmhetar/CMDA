#HW2 Ojas Mhetar


setwd('C:/Users/ojmhetar/Downloads')

#Importing the phSample data 
load('phsample.RData')

#This data set contains dhus and dpus
summary(dhus)
summary(dpus)

#There is a lot of variables with acorymns as headers and I cannot 
#truly understand what the data represents, and only take guesses. 

psub = subset(dpus, with(dpus, (PINCP>1000)&(ESR==1)&
    (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
    (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
    (PWGTP1>0)&(COW %in% (1:7))&(SCHL %in% (1:24))))

#The lines above take a subset of the larger data. We remove outliers 
#and focus on a specific sector of data.



psub$SEX = as.factor(ifelse(psub$SEX==1, 'M', 'F'))
psub$SEX = relevel(psub$SEX, 'M')
cowmap <- c("Employee of a private for-profit",
            "Private not-for-profit employee",
            "Local government employee",
            "State government employee",
            "Federal government employee",
            "Self-employed not incorporated",
            "Self-employed incorporated")
psub$COW = as.factor(cowmap[psub$COW])
psub$COW = relevel(psub$COW, cowmap[1])
schlmap = c(
    rep("No high school diploma", 15),
    "Regular high school diploma",
    "GED or alternative credential",
    "some college credit, no degree",
    "some college credit, no degree",
    "Associate's degree",
    "Bachelor's degree",
    "Master's degree",
    "Professional degree",
    "Doctorate degree")

#The above takes specific data from the earlier frame and classifies
#it into one of the headers. This allows the data to be read very easily.

psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL, schlmap[1])
dtrain =subset(psub, ORIGRANDGROUP >= 500)
dtest = subset(psub, ORIGRANDGROUP < 500)

#Another subset is taken so that the data is divided into 2 categories.

summary(dtrain$COW)

#The commands above summarize and arrange a large data of set so 
#that it can be easily understood

athletes <- read.table('OlympicAthletes_0.csv', sep=',', header=T)
  