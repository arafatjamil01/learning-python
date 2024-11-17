# Variables are dynamic
n = 5
print(n)

n = 'whatever'
print(n)

#multiple assignments
a, b = 1, 2
print(a, b)

n,m,z = 0.234, "hello", False
print(n, m, z)

# Increments
n=n+1 #good
n+=1 #good
# n+=  #bad

# Conditional statements
# Generally if statements don't need parentheses
m = 2
if m > 3:
    print('m is greater than 3.')
elif m == 3:
    print('m is equal to 3.')
else:
    print('m is less than 3.')

# Parentheses for multiline conditions
# In python && and || are replaced by 'and' and 'or'
x,y = 5,3
if( (x > 2 and y !=5) or y==3):
    print('This is true')

# while loop
n = 0
while n < 3:
    print(n)
    n += 1
    
# for loop
for i in range(5):
    print(i) # 0, 1, 2, 3, 4   Here 5 is not included
    
# for loop with specified range
for i in range(2,5):
    print(i) # 2, 3, 4   Here 5 is not included
    
# for loop with specified range and step
for i in range(5,1, -1):
    print(i) # 5, 4, 3, 2   Here 1 is not included
    
# Division is decimal by default
print(5/2) # 2.5

# Integer divisions
print(5//2) # 2, this rounds the number down to the nearest whole number

# Careful: most languages round towards zero, but python rounds towards negative infinity
print(-5//2) # -3

# A workaround for rounding towards zero
print(int(-5/2)) # -2, this results in 2.5 first, then int converts it to -2

# Modulus
print(10 % 3) # 1, this gives the remainder

# Modulus for negative numbers
print(-10 % 3) # 2, this is odd

# To match other languages, use this
import math
print(math.fmod(-10, 3)) # -1.0

# Math funcitons
print(math.floor(9/2))
print(math.ceil(9/2))
print(math.sqrt(9))
print(math.pow(2,3))

# Max / Min int
float("inf") # infinity
float("-inf") # negative infinity

# Python numbers are infinite, they never overflow
import math
print(math.pow(2, 1000)) # 1.0715086071862673e+301

print(math.pow(2,200) < float("inf")) # True

# Arrays (lists)
arr = [1,5.65,"hi",4,False]
print(arr)

# Can be used as stack, it is a dynamic array
arr.append(6)
print(arr)
arr.pop()
print(arr)

arr.insert(1,'inserted') # Big O(n) operation
arr[0] = 'changed' # Big O(1) operation, constant time operations
print(arr)

# Initialize an array of size n
n = 5
arr = [1] * n
print( arr)
print(len(arr))

# Negative indexing, to get from last element
print(arr[-1]) # last value
print(arr[-2]) # second last value

# Slicing or sublisting an array
arr = [1,2,3,4]
print(arr[1:3]) # 2,3 - this doesn't inlcude the last index
print(arr[0:4]) # 1,2,3,4 - this prints the full array, even though 4 is not in the index

# unpacking - valus of the array are assigned to the variables
a, b, c = [1, 2, 3]
print(a, b, c)

# a,b = [1,2,3] # this will throw an error, because number of items don't match the number of values in the list

# looping through the array
arr = ['w', 'o', 'r', 'd']

# method 1
for i in range(len(arr)):
    print(arr[i])

#method 2 
for i in arr:
    print(i)
    
# Using both index and value as variables
for i, val in enumerate(arr):
    print(i, val)
    
# Looping through multiple arrays silumtaneously
nums1 = [1,2,3]
nums2 = [4,5,6]

for n1, n2 in zip(nums1, nums2): # this combines the array value for each index and prints out
    print(n1, n2)
    
# Reverse an array
arr = [1,2,3,4]
print(arr[::-1]) # syntax is - arr[start:stop:step], here start and stop are not mentioned, so it takes the whole array
arr.reverse() # this reverses the actual array and saves in the same variable
print(arr)

# Sorting an array
arr = [3,1,4,2]
arr.sort() # this sorts the actual array in place, in ascending order
print(arr)
arr.sort(reverse=True) # this sorts the actual array in place, in descending order
print(arr)

# Sorting a string arrray
arr = ['word', 'apple', 'orange']
arr.sort()
print(arr)

# Custom sort by length of the string
arr.sort(key=len)
print(arr)

arr.sort(key=lambda x: len(x), reverse=True)
print(arr)

# List comprehension
arr = [i+i for i in range(5)] # The first i is the value, the second i is the loop variable
print(arr) # 0,1,2,3,4

# 2-D lists
arr = [[1,2,3], [4,5,6], [7,8,9]]
print(arr)

arr2 = [[0]*3 for _ in range(3)] # this creates a 3x3 array with all zeros, '_' is there instead of i, which is never used
print(arr2)

# bad example
# arr2 = [[0]*3]*3 # this creates a 3x3 array with all zeros, but all the rows are the same object, avoid this

# Strings are similar to arrays
s = "hello"
print(s[0]) # h
print(s[0:2]) # he

# s[0] = "K" # Strings are immutable, this will throw error
s += " world" # this creates a new string and assigns it to the variable, so this is n time operation
print(s)
 
# Valid numeric strings can be converter
print(int("123") + int("123"))

# Numbers can be converted to strings
print(str(456) + str(456))

# Getting the ASCII value of a char
print(ord("a")) # 97
print(ord("A")) # 65

# Combine a list off strings ( with an empty string #delimitor)
strings = ["ab","cd","ef"]
print("".join(strings)) # abcdef, nothing used as delimeter, you can use anything, space, hypen or anything you want

# Queues ( double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)