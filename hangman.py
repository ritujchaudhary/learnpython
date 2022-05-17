#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
empty_list =[]

for x in range(0,len(chosen_word)):
  empty_list.append("_")  

# guess = input("Guess a letter: ").lower()

print(empty_list)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
          empty_list[position] = letter
          
    # print(f"{' '.join(empty_list)}")
    if guess not in chosen_word:
      lives -= 1
      # print(stages[lives])

    # if guess in chosen_word:
    #   for position in range(word_length):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #       empty_list[position] = letter
    #   print(f"{' '.join(empty_list)}")  
    # else:
    #   lives -= 1
    #   print(stages[lives])
    #   #print(lives)
  
    if lives == 0:
      end_of_game = True
      print("lives over, you lose")

    print(f"{' '.join(empty_list)}")

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    #print(f"{' '.join(empty_list)}")

    #Check if user has got all letters.
    if "_" not in empty_list:
        end_of_game = True
        print("You win.")
  
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])