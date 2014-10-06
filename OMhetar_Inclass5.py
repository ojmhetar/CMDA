#Inclass5_1
'''
#1. iPython installed and running
2. Import modules pandas, numpy and matplotlib
Find out what functions each of them implement with the help of Tab Completion functionality. 
-Using the Tab Completion function, we can see that there are a ton of functions available
all you have to do is type the module and press tab twice.
3. Select 5 commands from these modules. Find a way to look for these function using ? and 
wildcards.
-I found the following commands: read_csv, read_fwf, read_table, dual, matlib
4. Use all the short-cut commands.
-Used all short cut commands to clear screen and refer to line input/output
5. Run all the magic commands.
-Ran all the magic commands and found them to be like basic command line utilities. 
6. Use your Inclass4_3, Part I and run snippets of code in iPython by copy-paste.
-Ran various snipets and I saw the appropriate output. 
7. Introspect magic command %xdel, function str.split, module re and matplotlib.pylab.
-?%xdel - Delete a variable, trying to clear it from anywhere that IPython's machinery has references to. 
-?str.split - Return a list of the words in the String S, using sep as the delimiter string. 
-module re*? - reduce, reload, repr, reversed
-matplotlib.pylab - written by John D. Hunter
8. Start pylab; build the plot on slide 10; do tab completion on numpy.;do introspection on 
numpy.random; find the line about randn. What type of numbers does it generate?
-It gives a list of utility functions, compatibility functions and other types of data
-randn generates normally distributed values
9. Find out what cumsum does.
-It Returns the cumulative sum of the elements along a given axis. 
10. How long does it take to generate 100 normally distributed random numbers? How about 
1000? How about 10,000?How did you find that out?(hint: run magic command timeit)
-100: 35.3 micro seconds
-1000: 34.8 micro seconds
-10000: 39.8 micro seconds
'''
#Inclass5_2
# coding: utf-8
# In[2]: import package
import numpy as np
# In[4]: Sets some array
array1 = np.array([1,3,5,3,1])
# In[5]: Same
array2 = np.array([4,3,5,1,2])
# In[8]: shows shape of array
print array1.shape
# In[9]: shows size of arary
array1.size
# In[10]: Add elementwise
array1 + array2
# In[11]: multiply element wise
array1 * array2
# In[13]: creates identity matrix
array6 = np.identity(6)
# In[14]: replays row 3 with 5s
array6[2] = [5,5,5,5,5,5]
# In[15]: 
array6
# In[16]: changes all values above 0 to 6
array6[array6 > 0] = 6
# In[17]:
array6
# In[22]: sets dimensions of empty array
arr3= np.empty((2,3,4), dtype=int)
# In[23]:
arr3
# In[25]:
arr3.shape
# In[26]:
arr3.dtype
# In[28]: changes a specific element to 5
arr3[1,1,0]=5
# In[33]: Creates an array with random variables 
arrRand = np.random.rand(20)
# In[34]:
arrRand
# In[35]: finds the minimum value in the array
arrRand.min()
# In[36]: finds the max value in the array
arrRand.max()
# In[37]: finds the sum
arrRand.sum()
# In[38]: finds average
arrRand.mean()
# In[39]: finds standard deviation
arrRand.std()
# In[47]:
np.where(arrRand > 0.5, 1,0)
# In[49]: Sorts the array
arrRand.sort()
# In[51]: finds unique values 
np.unique(arr3)





#Inclass5_3
# coding: utf-8
# In[1]: Import statements
import pandas
# In[4]:
import Quandl
# In[10]:
import numpy
# In[12]: Imports the dataframes
bitstamp = Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="1ewvkXDW7274TAdW7MoN")
# In[13]:
lakebtc = Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="1ewvkXDW7274TAdW7MoN")
# In[14]:
bitfinex = Quandl.get("BCHARTS/BITFINEXUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="1ewvkXDW7274TAdW7MoN")
# In[15]:
bitstamp.head()
# In[16]: Shows summaries of the data frames
lakebtc.head()
# In[17]:
bitfinex.head()
# #Columns are open, high, low, close, volume(BTC), volume(Currency) and Weighted Price. Frequency is daily
# In[20]: index of the data frames
ind1 = bitstamp.index
# In[21]:
ind2 = lakebtc.index
# In[22]:
ind3 = bitfinex.index
# In[23]:
ind1
# In[24]:
ind2
# In[25]:
ind3
# In[26]:
#ind1 and ind3 has 273 but ind2 has 214
# In[27]: shows the values attribute
ind1.values
# In[28]:
ind2.values
#### ind3.values
# In[29]:
ind3.values
# In[31]:
#JSON object is being displayed for values. The dtyle is a datetime
# In[32]:
bitstamp.columns
# In[33]:
lakebtc.columns
# In[34]:
bitfinex.columns
# In[35]:
#We have 7 colums in each.
# In[40]: Removes the Volume BTC column
bitstamp =bitstamp.drop('Volume (BTC)', 1)
# In[41]:
lakebtc=lakebtc.drop('Volume (BTC)', 1)
# In[42]:
bitfinex=bitfinex.drop('Volume (BTC)', 1)
# In[ ]:
