# # Definition of the generator to produce even numbers.
# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2

# my_gen = all_even()

# # Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))

# # Now go and do some other processing.
# do_something = 4
# do_something += 3
# print(do_something)

# # Now go back to generating more even numbers.
# for i in range(100):
#     print(next(my_gen))
    
def all_odd():
    n = 1
    while True:
        yield n
        n+=2

myOddFunc = all_odd()

for i in range(5):
    print(next(myOddFunc))
    
print('From the loop, the last number 9 will be remembered, if we do a next again - ')
print(next(myOddFunc))