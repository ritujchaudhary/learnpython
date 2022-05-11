import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = input('What do you choose? write Rock, Paper or Scissors.').lower()

if user == 'rock':
  print("you selected Rock\n")
  print(rock)
elif user == 'paper':
  print("you selected Paper\n")
  print(paper)
elif user == 'scissors':
  print("you selected scissors\n")
  print(scissors)

options = ['rock', 'paper', 'scissors']

com_sel = random.randint(0,2)

com_option = options[com_sel]

if com_option == 'rock':
  print("computer selected Rock\n")
  print(rock)
elif com_option == 'paper':
  print("computer selected Paper\n")
  print(paper)
elif com_option == 'scissors':
  print("computer selected Scissors \n")
  print(scissors)



if user == 'rock' and com_option == 'scissors':
  print("You win")
  
elif user == 'scissors' and com_option == 'paper':
  print("You win")

elif user == 'paper' and com_option == 'rock':
  print("You win")

elif user == com_option:
  print("its a DRAW")

else:
  print("You lose")



