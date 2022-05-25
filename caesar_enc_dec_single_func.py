alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text,shift_amount,code):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if code == "encode":
      new_position = position + shift_amount
    elif code == "decode":
      new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The text is {cipher_text}")

caesar(plain_text=text,shift_amount=shift,code=direction)