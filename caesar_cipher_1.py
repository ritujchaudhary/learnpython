alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(text,shift):
  text_list =[]
  
  ##take out each letter from input "text" and put it in a list
  for x in range(len(text)):
    text_list.append(text[x])
  #print(text_list)
  
  ##take an empty list
  index_list = []
  
  ##running a for loop untill length of text_list and 
  ##then comparing each item of text_list to the alphabet list 
  ##and getting postion of that letter from alphabet list and putting into separate list
  
  for letter in range(len(text_list)):
    for index in range(len(alphabet)):
      if text_list[letter] == alphabet[index]:
        index_list.append(index)
  #print(index_list)
  
  shift_index_list = []
  ## now we got all the corresponding indexes for input text from alphabet list
  ##so adding the shift it it and then generating new list
  for x in range(len(index_list)):
    if (index_list[x]+shift) >= len(alphabet):
      # x=-1
      shift_index_list.append(index_list[x]+shift-len(alphabet)+1)
    else:
      shift_index_list.append(index_list[x]+shift)
  ##got index shifted list
  #print(shift_index_list)
  
  ##encrypt msg:
  encrypt_msg = []
  
  for y in range(len(shift_index_list)):
    encrypt_msg.append(alphabet[shift_index_list[y]])
  
  #print(encrypt_msg)
  print(f"{' '.join(encrypt_msg)}")
  

encrypt(text,shift)
