### Conditionals ###

#IF

my_condition = False

if my_condition:  #This is the same that """if my_condition == True:"
    print("This is true")

my_condition = 5*5

if my_condition == 10:
    print("This is inside first if")

#if, elif, else

if my_condition > 10 and my_condition < 20:
    print("This number is higher than 10 and less than 20")
elif my_condition == 10:
    print("This is the same that my condition")
else:
    print("This is less or equals that 10 or higher or equals than 20 or distinct to 25")


print("This is out of the if's")

# Conditional whith value inspection

my_str = ""

if not my_str:
    print("This variable is empty")

if my_str == "My text strinnnnngggg":
    print("This text strings are the same")

### SHORT HAND

# code if condition else code

a =3
print("This is a postive number") if a > 0 else print("This is a negative number")

#print("This is a positive number") if a > 0 print("This is a negative numeber") elif a < 0 else print ("Is 0")

### NESTED CONDITIONS

#if condition:
#   code
#   if condition:
#       code

x = 0
if x > 0:
    if x % 2 == 0:
        print("X is a possitive and even integer")
    else:
        print("X is a positive number")
elif x == 0:
    print("X is zero")
else:
    print("X is a negative number")