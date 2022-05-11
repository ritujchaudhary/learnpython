# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
totalheight = 0

for i in student_heights:
    totalheight += i

no_of_stud = 0

for stud in student_heights:
    no_of_stud += 1

average = round(totalheight/no_of_stud)

print(average)
