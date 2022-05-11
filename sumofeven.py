###print sum of even numbers between 1 and 100

evensum=0
for num in range(1,101):
    if num%2==0:
        evensum +=num

print(evensum)


print("\n#######anotherway#######\n")

evensum=0
for num in range(2,101,2):
        evensum +=num

print(evensum)
