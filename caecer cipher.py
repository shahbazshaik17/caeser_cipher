alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-','.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-','.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',' ']

def caesar(start_text, shift_amount, cipher_direction):
   end_text = ""
   if cipher_direction == "decode":
      shift_amount *= -1
   for letter in start_text:
      new_position = alphabet.index(letter) + shift_amount
      end_text += alphabet[new_position]
   print(f"here's the {direction}d result: {end_text}")

from art import logo
print(logo)
should_end = False
while not should_end:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))
   shift = shift % 60
   caesar(text, shift, direction)
   
   restart = input("Type 'yes' to restart otherwise 'no': ")
   if restart == "no":
    should_end = True
   else:
    should_end = False
    print("Good bye")