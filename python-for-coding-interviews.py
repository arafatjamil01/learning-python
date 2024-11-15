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

# Seen up to 10:35