#list
li=["a","b","c",1]
print(f"the given list is {li}")
li.append(5)
print(f"the list after we append 5  at last is {li}")
li.remove("b")
print(f"the list after we remove element b {li}")
li[1]="h"
print(f"the list after we change first index element to h {li}")
print(f"the sliced list {li[1:3]}")
