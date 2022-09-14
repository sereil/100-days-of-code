#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from os import path

THIS_FOLDER = path.dirname(path.abspath(__file__))  

list_names = []
with open(f"{THIS_FOLDER}\\Input\\Names\\invited_names.txt") as names:
    for name in names.readlines():
        list_names.append(name.strip())


with open(f"{THIS_FOLDER}\\Input\\Letters\\starting_letter.txt") as data:
    letter = data.read()
    
    for name in list_names:
        new_letter = letter.replace("[name]",name)
        
        with open(f"{THIS_FOLDER}\\Output\\ReadyToSend\\Letter_To-{name}.txt",mode="w") as file:
            file.write(new_letter)


    
    
     