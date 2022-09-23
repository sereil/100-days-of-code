'''*args is unlimited positional arguments
*args will generate a tuple
https://www.upgrad.com/blog/list-vs-tuple/
'''
def add(*args):
    return sum(args)


# print(add(3,5,6))
'''
**kwargs is basically a dictionnary. If you print a **kwargs and get its type, it will give you a dict.
 '''
def calculate(n,**kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # pass
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2,add=3, multiply=5)

class Car:
    '''Instead of using indexing to retrieve a value, we can use .get() to access a key in a dictionnary.
    If this key is not found, it will return None instead of returning an error.
    '''
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"] #Essentially mandatory
        self.model = kwargs.get("model") #.get() makes this optional
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")
        

my_car = Car(make="Toyota")

print(my_car.make, my_car.model)
