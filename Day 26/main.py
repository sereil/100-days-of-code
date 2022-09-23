student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

nato_data = pandas.read_csv(".\\100-days-of-code\\Day 26\\nato_phonetic_alphabet.csv")
nato_alphabet = pandas.DataFrame(nato_data)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Type in a word to convert into a NATO Phonetic Alphabet List: ")

natoified_word = [nato_dict.get(letter.upper()) for letter in word]

print(natoified_word)