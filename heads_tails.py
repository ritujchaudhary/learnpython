import random

##randint(0,1) includes both number 0 and 1 and all numbers in between
random_num = random.randint(0,1)


##random.random(0,1) will produce all number between 0.00001.... to 0.99999.... and not including 1

if random_num == 1:
    print("heads")
else:
    print('tails')