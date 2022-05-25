#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area_of_wall = test_h * test_w
    # no_of_can = round(area_of_wall/cover)
    # print(f"You'll need {no_of_can} cans of paint.")
    no_of_can = math.ceil(area_of_wall/cover)
    print(f"You'll need {no_of_can} cans of paint.")
  

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


