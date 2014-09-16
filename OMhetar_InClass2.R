getwd()
setwd('C:/Users/ojmhetar/Downloads')
load('exampleData.rData')

summary(custdata)

#There are about 18 variables here

#In age, there seems to be an outlier because the mean is around 50, and the
#max is 146.7, it seems odd. 

#Also with age normized, the max is much higher than the rest of the values.

#Income normalized shows the trend again with a max much higher than the rest
#and so does income. 



uciCar <- read.table(
  'http://www.win-vector.com/dfiles/car.data.csv',
  sep=',',
  header=T
)

summary(uciCar)
#The numbers here are fairly consistent, with the number of high, low, and medium
#all being 432. 

# The amount of persons, lug_boot and safter all show 576.


load('credit.Rdata')
summary(d)

# There are 210 females who are divorced/separated/married while there are only
# 92 males who have been married/widowed. A large portion of males is single (548)

#It seems that most German loans do not require a co-applicant or guarantor, because
# there are 907 loans that have been done without one. 

install.packages("hexbin")
library(hexbin)

custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0))



x <- custdata2$age
y <- custdata2$income
bin<- hexbin(x, y, xbins=50)
plot(bin, main="Age vs income hexbin")

#This pot shows the density of the points much better than the 
#scatter plot. Very useful to see where the majority of people exist. 


#get a numerical summary of the relationship between the two
cor(custdata2$age, custdata2$income) #weak negative relationship


ggplot(custdata2, aes(x=num.vehicles,y=income)) +
  geom_point() +
  ylim(0,200000) +
  theme_bw() +
  ggtitle("Scatterplot of Num of vechiles vs age")
 
#I used a scatter plot to visualize the relationship between number of
#vehicles and income, however it may not be ideal because it only shows
#in rows. 

# I see that most people generally have 2 vechiles and a below 100,000 income.
#Oddly, those that have 6 vechiles also have under 100,000 income, which is strange
#because I would expect the opposite. 
#Also, those with 200k+ own 2 vehicles or less


custdata3 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0 & custdata$income < 30000))


ggplot(custdata3) + 
  geom_bar(aes(x=recent.move), fill = "green") +
  theme_bw() +
  ggtitle("Vertical Bar Chart")

#Using a Vertical Bar Chart, we can see that a majority of people with an
#income of less than 30k would be less likely to have moved recently. 