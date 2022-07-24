# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print(f"Hello")
#     print("How are you doing?")
#     print("Third print because idk why you need it.")

# #greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print("How are you doing?")
#     print("Third print because idk why you need it.")

# greet_with_name("Angela")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack","Japan")

#Prime Number Checker:
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for divisor in range (2,number):
        if number % divisor == 0:
            is_prime = False

    if is_prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
    
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


