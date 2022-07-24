#Caesar Cipher

#Day 8 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-24
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = art.logo
print(logo)
play_again = "yes"
while play_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if(shift > 26):
        shift = shift % 26 #Modulo of 26
        # example:
        # 45 % 26 = 19
        # 45 / 26 -> 26 can fit inside 45 once, with a remainder of 19

    def caesar(plain_text, shift_amount, cipher_direction):
        cipher_text = ""         
        if cipher_direction == "decode":
                shift_amount *= -1 #nice way to avoid doing this twice for adding and negating: position = alphabet.index(letter) -+ shift_amount  
        for letter in plain_text:
            if(letter not in alphabet):
                cipher_text += letter
            else:
                position = alphabet.index(letter) + shift_amount
                new_character = alphabet[position]
                cipher_text += new_character    
        print(f"The {cipher_direction}d text is '{cipher_text}'")        
    caesar(cipher_direction=direction, plain_text=text, shift_amount=shift)

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()    
    if play_again == 'no':
        print("Goodbye.")