#list comprehension
li=[x for x in range(10)]
print(f"the list using list comprehension is {li}")
#list comprehension with condition
li=[x for x in range(10) if x%2==0]
print(f"the list using list comprehension with condition is {li}")
#list comprehension with condition and operation
li=[x**2 for x in range(10) if x%2==0]
print(f"the list using list comprehension with condition and operation is {li}")
#list comprehension with nested loop
li=[x*y for x in range(1,5) for y in range(1,5)]
print(f"the list using list comprehension with nested loop is {li}")
#list comprehension with if else
li=[x if x%2==0 else x**2 for x in range(10)]
print(f"the list using list comprehension with if else is {li}")