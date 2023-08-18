### Exeption Hadling ###

first_number, second_number = 5, "5"


# try execpt
try:
    print(first_number + second_number)
    print("There isn't a error")
except: #runs if an error occurs (if an exeption occurs)
    print("There is a error")

# try except else

try:
    print(first_number + second_number)
    print("There isn't a error")
except:
    print("There is a error")
else:   #runs if not an error occurs (if not an exception occurs)
    print("The execution continues")

# try except else finally

try:
    print(first_number + second_number)
    print("There isn't a error")
except:
    print("There is a error")
else:   #runs if not an error occurs (if not an exception occurs)
    print("The execution continues")
finally:    # always runs
    print("The execution continues")


# Exeption by type
try:
    print(first_number + second_number)
    print("There isn't a error")
except TypeError:   # With TypeError the exeption only runs when the type of the error is TypeError
    print("There is a TypeError")
except ValueError:
    print("There's a ValueError")

# Capture the exception information


try:
    print(first_number + second_number)
    print("There isn't a error")
except ValueError as error: # With as "x" you save more information about the error in a variable
    print("This is a ValueError")
    print(error)
except Exception as error2:
    print(error2)