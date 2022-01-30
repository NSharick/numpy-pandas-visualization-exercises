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
import matplotlib as plt

letters.value_counts().head(6)
#pulls the six most frequently occurring strings from the series
six_most = letters.value_counts().head()
#assigns a variable to the above data
six_most.plot(kind= 'barh', color= 'green')
plt.pyplot.title('Six Most Commonly Occurring Letters')


####################


number_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
numbers = pd.Series(number_list)
print(numbers)

#1 -- What is the data type of the numbers Series?
numbers.dtype
#returns -- dtype('O')


#2 -- How many elements are in the number Series?
numbers.size
#returns -- 20


#3 -- Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
#remove the '$' and the commas the change the data type to float
nums = numbers.str.replace('$', '').str.replace(',', '').astype('float')
#verify the return values and the return data type
print(nums)
nums.dtype


#4 -- Run the code to discover the maximum value from the Series.
nums.max()
#returns 4789988.17


#5 -- Run the code to discover the minimum value from the Series.
nums.min()
#returns 278.6


#6 -- What is the range of the values in the Series?
nums.index
#returns -- RangeIndex(start=0, stop=20, step=1)


#7 -- Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(nums, 4)
#returns --
#0        (-4511.11, 1197705.993]
#1        (-4511.11, 1197705.993]
#2        (-4511.11, 1197705.993]
#3      (3592560.778, 4789988.17]
#4     (1197705.993, 2395133.385]
#5     (1197705.993, 2395133.385]
#6        (-4511.11, 1197705.993]
#7     (1197705.993, 2395133.385]
#8      (3592560.778, 4789988.17]
#9     (2395133.385, 3592560.778]
#10       (-4511.11, 1197705.993]
#11     (3592560.778, 4789988.17]
#12     (3592560.778, 4789988.17]
#13    (2395133.385, 3592560.778]
#14    (1197705.993, 2395133.385]
#15     (3592560.778, 4789988.17]
#16     (3592560.778, 4789988.17]
#17    (2395133.385, 3592560.778]
#18       (-4511.11, 1197705.993]
#19       (-4511.11, 1197705.993]
#dtype: category
#Categories (4, interval[float64, right]): [(-4511.11, 1197705.993] < (1197705.993, 2395133.385] < (2395133.385, 3592560.778] < (3592560.778, 4789988.17]]

#group and sort the binned values and assign it to a variable
bin_nums = pd.cut(nums, 4).value_counts().sort_index()
print(bin_nums)
#returns --
#(-4511.11, 1197705.993]       7
#(1197705.993, 2395133.385]    4
#(2395133.385, 3592560.778]    3
#(3592560.778, 4789988.17]     6
#dtype: int64


#8 -- Plot the binned data in a meaningful way. Be sure to include a title and axis labels.#

#plot the above bunned values
bin_nums.plot(kind= 'barh', color= 'red')
plt.pyplot.xlabel('numbers in group')
plt.pyplot.ylabel('group value range')
plt.pyplot.title('$ value in four groups')


############################

examscores = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series(examscores)

#1 - How many elements are in the exam_scores Series?
exam_scores.size
#returns -- 20


#2 - Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.describe()
#returns -- 
#count    20.000000
#mean     78.150000
#std      11.352139
#min      60.000000
#25%      70.500000
#50%      79.000000
#75%      85.250000
#max      96.000000
#dtype: float64

exam_scores.min()
#returns -- 60
exam_scores.max()
#returns -- 96
exam_scores.mean()
#returns -- 78.15
exam_scores.median()
#returns -- 79.0


#3 - Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
#plot the original exam scores in a histogram to show overall score distribution
exam_scores.plot.hist(color= 'blue')
#add titles
plt.pyplot.title('Exam Grades')
plt.pyplot.ylabel('number of students')
plt.pyplot.xlabel('grade range')

#bin the values by standard letter grade ranges then count the values in each range and sort by the index
bin_scores = pd.cut(exam_scores, [50, 60, 70, 80, 90, 100]).value_counts().sort_index()
#plot the binned values in a bar graph
bin_scores.plot(kind= 'barh', color= 'blue')
#add titles
plt.pyplot.title('Exam Grades')
plt.pyplot.xlabel('number of students')
plt.pyplot.ylabel('grade range')


#4 - Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
#find the curve value
curvegrade = 100 - exam_scores.max()
print(curvegrade)
#make a list of the grades with a curve
curve_grades = exam_scores + curvegrade
print(curve_grades)


#5 - Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
bin_curve_scores = pd.cut(curve_grades, [50, 60, 70, 80, 90, 100]).value_counts().sort_index()
print(bin_curve_scores)


#6 - Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
#plot the binned cureved grades
bin_curve_scores.plot(kind= 'barh', color= 'green')
#add titles
plt.pyplot.title('Exam Grades With Curve')
plt.pyplot.xlabel('number of students')
plt.pyplot.ylabel('grade range')

