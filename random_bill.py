###Banker Roulette

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num = len(names)
pick_index = random.randint(0,num-1)
pick_name = names[pick_index]
print(f"{pick_name} is going to buy the meal today!")