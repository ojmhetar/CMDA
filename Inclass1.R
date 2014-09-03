getwd()
setwd("C:/Users/ojmhetar/Dropbox/Virginia Tech/Junya/CMDA")

#Importing cars1.csv dataset 
carscsv<- read.table('cars1.csv', sep=',', header=T)

#Show dimension of the data frame
dim(carscsv)

#Assigns value in cell [2,2] to a variable
var1<-carscsv[2,2]

#Prints the variable names of the data base
colnames(carscsv)

#Outputs first column
carscsv[,1]

#Outputs the second column
carscsv[,2]

#assign vlues of variable speed into new variable SPEED
SPEED<-carscsv$speed

#prints out variable SPEED
SPEED

#Prints out the value of row 15
carscsv[15,]
