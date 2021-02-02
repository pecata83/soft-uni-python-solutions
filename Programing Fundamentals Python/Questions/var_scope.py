# How variables scope in python works and is there any hoisting like in JS.

# 1
for i in range(1):
    some_var = "Ivan"

# Variable is accessible outside for loop scope
print(some_var)

# 2


def create_name():
    name = "Petar"
    print(name)


create_name()
print(name)
