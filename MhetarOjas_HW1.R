#Ojas Mhetar  8/30/2014 CS3654 HW1
#My github account: https://github.com/ojmhetar

getwd()
setwd("C:/Users/ojmhetar/Downloads")


#Problem 1

#To read without header value
pricescsv<- read.table('prices.csv', sep=',', header=F)

#To read with headers
pricescsv<- read.table('prices.csv', sep=',', header=T)

#Change the colnames 
colnames(pricescsv)<-c('PRICE','SQFT','AGE', 'NE')


pricescsv

#row.names sets a variable with all the values in the first column
rowname = row.names(pricescsv)


mydatatxt<- read.table('prices.txt', sep='\t', header=T)

#creating a sample table
samplefile<- read.table('sampHW1.txt', sep='\t', header=T)



#Problem 2

#Create a 4by4 Matrix
c1 = c(1, 1, 2, 4)
c2 = c(2, 2, 2, 4)
c3 = c(0, 1, 0, 3)
c4 = c(0, 1, 0, 2)
mat4=cbind(c1,c2,c3,c4)

lastrow=mat4[4,]

transpose = t(mat4)

inverse = solve(mat4)

#Problem 3

fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")

#prints columns where there is 0 effort
fpe[fpe$effort == 0,]


names(fpe)
rownames(fpe)


?head

head(fpe)

#From R to a csv file
write.csv(fpe,file="sampRHW1.csv") 
#From R to a text document
write.table(fpe,file="sampRHW1Txt.txt", sep="\t")
