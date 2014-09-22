
setwd("C:/Users/ojmhetar/Downloads")


athletes <- read.table('OlympicAthletes_0.csv', sep=',', header=T)

summary(athletes)
#Data is distributed fairly evenly, I don't see any real changes
#that need to be made. 

install.packages('ggplot2')

library(ggplot2)

ggplot(athletes) +
  geom_histogram(aes(x=Country),
                 binwidth = 5)+
  theme_bw()

#Above is how many times a country has participated

ggplot(athletes) +
  geom_density(aes(x=Age)) +
  theme_bw() +
  ggtitle("Density plot")

#Above is a desnity plot of the age of athletes that participate


ggplot(athletes, aes(x=Age,y=Total.Medals)) +
  ylim(0,10) +
  geom_point() +
  geom_smooth()+
  ggtitle("Scatterplot of Age vs Total Medals") +
  theme_bw() 

#Above plots a scatterplot of the age of atheletes and the total medals they've won.


#age <- transform(age, Age=reorder(Age,count))
#No treatments needed, but if they were it would look like above line.

