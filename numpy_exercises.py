## numpy exercises ##

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1
#how many negative numbers are there in the array
len(a[a < 0])
# returns 4

#2
#how many positive numbers are there
len(a[a > 0])
#returns 5

#3
#how many even positive numbers are there
x = a[a > 0]
y = x[x % 2 == 0]
len(y)
#returns 3

#4
#if you added three to each how many positives would there be?
#add three to each from the original array
b = a + 3
#count (len()) the array with only numbers greater than 0
len(b[b > 0])
#print to verify
print(b)

#5
#square all the numbers in the array
c = a ** 2
#get the mean of the new array
c.mean()
#get the standard deviation of the new array
c.std()

#6
#centering the values in the original array
#create a new array with the mean subtracted from the original values
d = a - a.mean()
#verify the new mean is centered (0.0)
d.mean()

#7
#calculate the z score for each data point
z_score = (a - a.mean()) / a.std()
#print to verify
print(z_score)

##8 -- More Numpy Practice ############################################################################

# Life w/o numpy to life with numpy

## Setup 1
a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = a2.sum()
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a2.min()
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a2.max()
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a2.mean()
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a2.prod()
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a2 ** 2
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a2[a2 % 2 != 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a2[a2 % 2 == 0]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_b = b.sum()
print(sum_b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_b = b.min()
print(min_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_b = b.max()
print(max_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_b = b.mean()
print(mean_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_b = b.prod()
print(product_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_b = b ** 2
print(squares_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_b = b[b % 2 != 0]
print(odds_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_b = b[b % 2 == 0]
print(evens_b)

# Exercise 9 - print out the shape of the array b.
np.shape(b)
print(np.shape(b))

# Exercise 10 - transpose the array b.
b.transpose()

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1, 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6, 1)

## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c.min() # 1
c.max() # 9
c.sum() # 45
c.prod() #362880

# Exercise 2 - Determine the standard deviation of c.
c.std() #2.581988897471611

# Exercise 3 - Determine the variance of c.
c.var()

# Exercise 4 - Print out the shape of the array c
np.shape(c)

# Exercise 5 - Transpose c and print out transposed result.
c.transpose()
print(c.transpose())

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
np.sum(c * (c.transpose()))

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.prod(c * (c.transpose()))

## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

# Exercise 4 - Find all the negative numbers in d
d[d < 0]

# Exercise 5 - Find all the positive numbers in d
d[d > 0]

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))

# Exercise 8 - Print out the shape of d.
np.shape(d)

# Exercise 9 - Transpose and then print out the shape of d.
np.transpose(d)
print(np.transpose(d))

# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9, 2)
print(d.reshape(9, 2))
