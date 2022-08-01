###############DEBUGGING##################
##########################################
# # # # # # Describe Problems # # # # # #
##########################################

#The second parameter of the range function is exclusive and i wil never reach 20.
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
#
# from random import randint
#randint(1,6) will do numbers betwen 1 and 6 (1,2,3,4,5,6)
#change to randint(0,5)
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
#1994 will is never captured, one of them needs to be >= or <=
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# Indent error
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")

# #Print is Your Friend
 #There was an == statement instead of a variable declaring for word_per_page.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
#b_list.append only happens after the for loop is done running. 
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])