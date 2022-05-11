# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

##convert to int
position = int(position)

#Write your code below this row 👇
row = (position%10) -1
column = (position//10) -1

if row == 0:
    row1[column]="X"
elif row ==1:
    row2[column]="X"
elif row ==2:
    row3[column]="X"
else:
    print("invalid")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


##########################another way to do it ##################
## eg. below selecting '2' and '3' as strings from '23' input string
##convert to string
print("############alternaly##############")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal -1 ] = 'X'

##or map[vertical -1][horizontal -1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

