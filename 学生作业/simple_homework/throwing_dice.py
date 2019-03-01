import random
def throw24():
    for i in range(24):
        a=random.choice(range(1,7))
        b=random.choice(range(1,7))
        if a==6 and b==6:
            return 1
    return 0

times=input('How many times do you want to try ? blank input means defualt 10000\n')
if times=='':
    times=10000
else:
    times=int(times)
twosixs=0
for i in range(times):
    twosixs=twosixs+throw24()
print('the probability is %s' % (twosixs/times))