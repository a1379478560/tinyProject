# These two functions imitate the random.randint function
# so we can test our code on specific sequences of inputs

# Test 1
#VALUES = [3,4,1,2,5,6,2,3,2,2,3,3,1,4,2,4,2,3,4,5,3,4]
VALUES = [0,1,3,2,9,0,1,3,2,9,0,1,3,2,9,0,1,3,2,9,0,1,3,2,9,0,1,3,2,9]
# rand is a generator function
# each time you call it you get the next value in the list of numbers
rand = (i for i in VALUES)

# rand is called using the next() function
# we wrap it in our randint() function so we can use it in our program
def randint(a,b):
    '''return the next value in the rand generator.
    for testing the parameters a and b are ignored.'''
    return next(rand)