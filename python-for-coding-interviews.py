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





