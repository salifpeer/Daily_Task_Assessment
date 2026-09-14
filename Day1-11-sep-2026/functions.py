#function with postional arguments
def add(a,b):
    return a+b
print(f"the sum of 10 and 20 is {add(10,20)}using function with postional arguments")
#function with default arguments
def add(a,b=10):
    return a+b  
print(f"the sum of 10 and 20 is {add(10,20)}using function with default arguments")
print(f"the sum of 10 and 10 is {add(10)}using function with default arguments")
#function with keyword arguments
def add(a,b):
    return a+b 
print(f"the sum of 10 and 20 is {add(b=20,a=10)}using function with keyword arguments")
#functions with arbitrary number of arguments
def add(*args): 
    sum=0
    for i in args:
        sum+=i
    return sum
print(f"the sum of 10,20,30,40 is {add(10,20,30,40)}using function with arbitrary number of arguments")
#function with arbitrary number of keyword arguments
def add(**kwargs):
    sum=0
    for i in kwargs.values():
        sum+=i
    return sum  
print(f"the sum of 10,20,30,40 is {add(a=10,b=20,c=30,d=40)}using function with arbitrary number of keyword arguments")