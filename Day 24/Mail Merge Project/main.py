#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

list_names = []
with open(".\\Input\\Names\\invited_names.txt") as names:
    for name in names.read():
        list_names.append(name)


with open(".\\Input\\Letters\\starting_letter.txt") as data:
    letter = data.read()
    
    for name in list_names:
        print(letter.replace("[name]",name))
    
    
     