'''Exercise 1 - Squaring Numbers'''

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

#Write your code 👆 above:

#print(squared_numbers)

'''Exercise 2 - Filtering Even Numbers'''

#Write your 1 line code 👇 below:

even_numbers = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:
print(even_numbers)


list1 = [3,6,5,8,33,12,7,4,72,2,42,13]
list2 = [3,6,13,5,7,89,12,3,33,34,1,344,42]

# with open("file1.txt") as file1:
#     list1 = file1.readlines()
# with open("file2.txt") as file2:
#     list2 = file2.readlines()

result = [int(num) for num in list1 if (num in list2)]

# Write your code above 👆

print(result)


