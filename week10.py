# Pratice Exercises
# Question 1 Week 10
#Numpy Array mauipulation
import numpy as np

myArray = np.array([1, 2, 3, 4, 5])
# basic indexing
print(myArray[2])
print(myArray[0:2])

# Resahping an array
print(myArray.reshape(1, 5))

# Splitting an array
print(np.split(myArray, 5))

# Question 2 Week 10
# Mathematical Operations with numpy

# Using array to calculate the mean
print(np.mean(myArray))

# Using array to calculate the standard deviation
print(np.std(myArray))

# Using array to calculate the square 
print(np.square(myArray))

#Question 3 Week 10
# Matrix multiplication with Numpy
matrix1 = np.array([[3, 7, 5], [2, 8, 4]])
matrix2 = np.array([[1, 2, 5], [3, 4, 6], [9, 8, 7]])
print(np.dot(matrix1, matrix2))
print(matrix1 @ matrix2)
