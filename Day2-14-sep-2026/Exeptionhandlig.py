#zerodivision exception
try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
#try with multiple except blocks
try:
    a=[1,2,3]
    print(a[5])
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except IndexError:
    print("Error: Index out of range.")
#try with else block
try:
    a=10
    b=2
    c=a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"the result of the division is {c}")
#universal exception handling
try:
    with open("abc.txt", "r") as file:
        content = file.read()   
except Exception as e:
    print(f"An error occurred: {e}")
#raising exception
def divide(a,b):   
    if b==0:
        raise ValueError("Division by zero is not allowed.")
    return a/b
#raising exception with try except block
try:
    result=divide(10,0)
    print(f"the result of the division is {result}")
except ValueError as e:
    print(f"Error: {e}")
#userdefined exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message  

def login(username, password):
    if username != "admin" or password != "password":
        raise CustomError("Invalid username or password.")
    print("Login successful.")
try:
    login("user", "pass")
except CustomError as e:
    print(f"Error: {e}")
