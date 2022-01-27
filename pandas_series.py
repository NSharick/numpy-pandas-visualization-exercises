### Pandas Series Exercises###

import numpy as np
import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


###Exercise Part 1###########################################################

#1 Determine the number of elements in fruits.
fruits.size
#returns the size of the array -- 17

#2 Output only the index from fruits
fruits.index
#returns the index of the series -- RangeIndex(start=0, stop=17, step=1)

#3 Output only the values from fruits.
fruits.values
#returns the valuse in the series -- 
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple','honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi','kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry','papaya'], dtype=object)

#4 Confirm the data type of the values in fruits
fruits.dtype
#returns the type of data in the array -- dtype('O')


#5 Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head()
#returns the first five values (5 is the default number of items returned)
fruits.tail(3)
#returns the last three fruits in the list since three was defined in the parentheses
fruits.sample(2)
#returns a random sample of two values as called


#6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()
#returns info on the array -- 
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object


#7/8 Run the code necessary to produce only the unique string values from fruits / Determine how many times each unique string value occurs in fruits.
fruits.unique
#returns a list of the unique values from the array
fruits.value_counts()
#returns unique values from the array with a count of how many times each appears in the array --
#kiwi                4
#mango               2
#strawberry          1
#pineapple           1
#gala apple          1
#honeycrisp apple    1
#tomato              1
#watermelon          1
#honeydew            1
#blueberry           1
#blackberry          1
#gooseberry          1
#papaya              1
#dtype: int64


#9 Determine the string value that occurs most frequently in fruits.
(fruits.value_counts()).sort_values(ascending= False)
#the above takes the value counts and sorts the return values in decending order so that the fruit that occurs most frequently is at the top of the list
fruits.value_counts().nlargest(n= 1)
#the above takes the array with the value counts and returns the one that occurs the most 
# -- 'kiwi 4'


#10 Determine the string value that occurs least frequently in fruits.
(fruits.value_counts()).sort_values()
#the above takes the value counts and sorts the return values in ascending order so that the fruit that occurs least frequently is at the top of the list
fruits.value_counts().nsmallest(n= 17) #used '17' since we got that for the above exercise checking the array size.
#running the above shows that most fruits only occur once so to get a list of all the fruits that "tie" for lease frequent we can run:
fruits.value_counts().nsmallest(n= 11)
#which returns --
#strawberry          1
#pineapple           1
#gala apple          1
#honeycrisp apple    1
#tomato              1
#watermelon          1
#honeydew            1
#blueberry           1
#blackberry          1
#gooseberry          1
#papaya              1
#dtype: int64

#the best way to run it is like this:
fruits.value_counts().nsmallest(n= 1, keep= 'all')
#the 'keep = all' returns all the values if there are duplicates - in this case there were 11 fruits with only one occurrence



###Exercise Part 2###############################################################

#1 -- Capitalize all the string values in fruits.
fruits.str.capitalize()
#returns the array values with the strings capitalized
fruits.str.upper()
#returns the array with the values in all caps
fruits.str.lower()
#returns the array with all the values in lowercase


#2 Count the letter "a" in all the string values (use string vectorization)
fruits.str.count('a')
#returns the count of 'a's in each word in the array --
#0     0
#1     1
#2     1
#3     1
#4     3
#5     1
#6     1
#7     1
#8     0
#9     0
#10    0
#11    0
#12    1
#13    0
#14    1
#15    0
#16    3
#dtype: int64


#3 -- Output the number of vowels in each and every string value
fruits.str.count('a', 'e', 'i', 'o', 'u') #Does not work because of too many arguments
#works but long
fruits.str.count('a') + fruits.str.count('e') + fruits.str.count('i') + fruits.str.count('o') + fruits.str.count('u')
#best way!
fruits.str.count('[aeiou]')


#4 Write the code to get the longest string value from fruits
fruits.str.len().max()
#returns the length of the longest string in the series -- 16
max(fruits, key= len)
#returns the value of the longest string -- ['honeycrisp apple']


#5 -- Write the code to get the string values with 5 or more letters in the name
fruits.str.len() >= 5
#this will return the string of booleans and wrapping it with the series name and the brackes will return the values from the series.
fruits[fruits.str.len() >= 5]
#returns --
#1                mango
#2           strawberry
#3            pineapple
#4           gala apple
#5     honeycrisp apple
#6               tomato
#7           watermelon
#8             honeydew
#12               mango
#13           blueberry
#14          blackberry
#15          gooseberry
#16              papaya
#dtype: object


#6 -- Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits.apply(lambda f: f.count('o') > 2)
#returns all false because there are not any values with more than 2 'o
fruits.apply(lambda f: f.count('o') > 1)
#returns 2 'true'
fruits[fruits.apply(lambda f: f.count('o') > 1)]
#returns the two values with more than on 'o'
#6         tomato
#15    gooseberry
#dtype: object


#7 -- Write the code to get only the string values containing the substring "berry"
fruits[fruits.str.contains('berry')]
# returns --
#2     strawberry
#13     blueberry
#14    blackberry
#15    gooseberry
#dtype: object


#8 -- Write the code to get only the string values containing the substring "apple"
fruits[fruits.str.contains("apple")]
#returns -- 
#3           pineapple
#4          gala apple
#5    honeycrisp apple
#dtype: object
fruits[fruits.str.contains(" apple")]
#adding the whitespace before the word 'apple' will only return the two apples --
#4          gala apple
#5    honeycrisp apple
#dtype: object


#9 -- Which string value contains the most vowels?
fruits[max(fruits.str.count('[aeiou]'))]
#returns -- 'honeycrisp apple'


###Exercises Part 3###############################################

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
print(letters)

#1 -- Which letter occurs the most frequently in the letters Series?
letters.value_counts()
#returns the counts for each nuique value

x = letters.value_counts()
[x.nlargest(n= 1)]
#or
letters.value_counts().nlargest(n= 1)
#returns 'y 13'


#2 -- Which letter occurs the Least frequently?
x = letters.value_counts()
[x.nsmallest(n= 1)]
#or
letters.value_counts().nsmallest(n= 1)
#returns 'l 4'


#3 -- How many vowels are in the Series?
sum(letters.str.count('[aeiou]'))
#returns -- 34
#best practice to chain the sum() onto the statement rather than wrap it around the statement
letters.str.count('[aeiou]').sum()


#4 -- How many consonants are in the Series?
letters.str.count('[^aeiou]').sum()
#the '^' works as a 'not'
#returns 166


#5 -- Create a Series that has all of the same letters but uppercased
letters.str.upper()
#returns all strings in uppercase


#6 -- Create a bar plot of the frequencies of the 6 most commonly occuring letters
letters.value_counts().head(6)
#pulls the six most frequently occurring strings from the series
six_most = letters.value_counts().head()
#assigns a variable to the above data












##Part 2 #########

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
print(numbers)

#1 -- What is the data type of the numbers Series?

#2 -- How many elements are in the number Series?

#3 -- Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

#4 -- Run the code to discover the maximum value from the Series.

#5 -- Run the code to discover the minimum value from the Series.

#6 -- What is the range of the values in the Series?

#7 -- Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

#8 -- Plot the binned data in a meaningful way. Be sure to include a title and axis labels.#


