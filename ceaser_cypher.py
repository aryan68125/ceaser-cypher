#this program will encrypt the message or decrypt the message using ceaser cipher technique
import alphabet

#download and install art pip3 install art in your linux machine or mac osX then import art
from art import *
welcome_message1=text2art("message") # Return ASCII text (default font) and default chr_ignore=True 
print(welcome_message1)
print("\n")
welcome_message2=text2art("encryption") # Return ASCII text (default font) and default chr_ignore=True 
print(welcome_message2)
print("\n")
welcome_message3=text2art("decryption") # Return ASCII text (default font) and default chr_ignore=True 
print(welcome_message3)
print("\n")

for i in range(0,1000):

    #select the mode 
    direction = input("Type 'encode' to encrypt, Type 'decrypt' to decrypt the message\n")
    #.lower() converts the message to lower case letters
    text = input("Enter the message\n").lower()
    #the shift formula for encryption or decryption of messages
    shift = int(input("Enter the shift number\n"))

    #encrypt function
    def encrypt(message,shift_amount):
        #create an empty string to hold a cipher text 
        encrypt.cipher_text = ""
        # a loop used to iterate through each individual characters of a string 
        for char in message:
            # now we will try to get the position of each character in our character list module
            # encrypt.x will create an trribute of the function of the variable so that we can access it outside the function
            # alphabet.alphabet acessing alphabet list from alphabet module
            if char is not ' ':
                if char in alphabet.alphabet:
                    position = alphabet.alphabet.index(char)
                    new_position = position + shift_amount
                    new_char = alphabet.alphabet[new_position]
                    encrypt.cipher_text += new_char
                else:
                    encrypt.cipher_text += char
            else:
                encrypt.cipher_text += ' '

    #decrypt function
    def decrypt(cipher_text,shift_amount):
        #create an empty string to hold a message text 
        decrypt.message_text = ""
        # a loop used to iterate through each individual characters of a string 
        for char in cipher_text:
            # now we will try to get the position of each character in our character list module
            # encrypt.x will create an trribute of the function of the variable so that we can access it outside the function
            # alphabet.alphabet acessing alphabet list from alphabet module
            if char is not ' ':
                if char in alphabet.alphabet:
                    position = alphabet.alphabet.index(char)
                    new_position = position - shift_amount
                    new_char = alphabet.alphabet[new_position]
                    decrypt.message_text += new_char
                else:
                    decrypt.message_text += char
            else:
                decrypt.message_text += ' '

    #display function
    def display(choice):
        #converting choice in lower case 
        lower_choice = choice.lower()
        if lower_choice == "encode":
            encrypt(message=text, shift_amount=shift)
            print(f"the encrypted message is = {encrypt.cipher_text}")
  
        if lower_choice == "decode":
            decrypt(cipher_text=text, shift_amount=shift)
            print(f"the decrypted message is = {decrypt.message_text}")
    display(choice=direction)
    print("press q to quit or enter to continue:->")
    q=input()
    if q=='q' or q=='Q':
        break