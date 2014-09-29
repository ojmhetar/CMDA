#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#displays the text within the quotes to the prompt.
print "I will now count my chickens:"

#displays "Hens" to the screen then computes the expression to result in 30
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

#Prints the text within the quotes to the screen. 
print "Now I will count the eggs:"

#Evaluates and prints the result: 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#Prints the text within the quotes to the screen
print "Is it true that 3 + 2 < 5 - 7?"

#Evaluates the expression and prints the result,False, to the screen
print 3 + 2 < 5 - 7

#Prints the text first and then computes the expression and prints that after
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

#The next two lines just print the text to the screen
print "Oh, that's why it's False."
print "How about some more."

#Prints the text then evaluates the expression resulting in, True, True, False
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#PART II

#Stores the days of the week in the variable day. Also stores the months with a new line space in the
#months variable.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#prints the days variable, prints the months variable (vertically arranged)
print "Here are the days: ", days
print "Here are the months: ", months

#PART III

#Uses a variable to store an array that contain elements
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Loops (runs the same line of code) for the length of the array and prints every element %d for integer
#This is count 1, This is count 2, etc.
for number in the_count:
    print "This is count %d" % number

# Loops through the array and prints each element to the screen. 
#A fruit of type apples, A fruit of type oranges, etc. 
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Loops and prints all the elements in the change array even though they have different
#types of variables in them.
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# prints out the values held in the elements array (0 through 6)
for i in elements:
    print "Element was: %d" % i

#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is
stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#Day
print stuff[1]
#Boy
print stuff[-1] 
#Boy, removes last element from array
print stuff.pop()
#Prints all the elements with a space inbetween 
print ' '.join(stuff) 
#Prints elements 3 through 5 with a # inbetween. 
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# creates an new JSON object of states and their abreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# creates a new JSON object of cities and their abreviations
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# modifies the object to make additions, adds New York and Portland
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Prints a line of dashes, then prints text followed by any matches of 'NY' and same for second line, but for 'OR'
#So, it shows that they each have a specific city
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Prints a line of dashes. 
#Then after the text it prints the abreviation of the state by searching for a key that matches 'Michigan'
#and then 'Florida' respectively. Thus, the abreviation is displayed. 
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Prints a line of dashes. The inner expression determines the abreviation for the state, then the abreviation 
#is used to search for cities associated with that abreviation. 
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Prints a line of dashes. Loops through all the elements in the state object
# and display the state with its associated abreviation.
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Prints a line of dashes. Loops through all the elements in the city object
# to display each abreviation with the respective city.
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Prints the standard line of dashes. Loops through all the elements again and lists all the information.
# In addition to just the state and abreviation, it also searchs the cities array with the abreviation
# to display the city information also. 
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



