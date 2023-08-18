### Functions ###

def my_function():
    print("Hello World")


def sum_two_values(first_num, secound_num):
    print(first_num + secound_num)


my_function()

sum_two_values(2, 6)


# Function with input/output parameters

def sum_two_values_with_return(first_num, secound_num):
    x = first_num + secound_num
    return x

var_returned = sum_two_values_with_return(10, 4) #This is the way to get the result of the function. You can't get the result of the funcition without return
print(var_returned)

# Function with input parameters/arguments by key
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Portillo", name = "Michael")

# Function with default input parameters/arguments

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Michael", "Portillo")
print_name_with_default("Michael", "Portillo", "Raptor")

# Function with arbitrary input parameters/arguments

def print_texts(*text): # When you'll pass undifined arguments "*"
    print (type (text))
    for i in text:
        print(i.upper())

print_texts("Hello World" , "Python", "C++") 



def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27