variable = "hola", 5, False
print(type(variable))

variable1 = "Hello World"
variable2 = 7
variable3 = True


#Concatenacion 1
print(variable1, variable2, variable3)

#concatenacion 2
print(f"Hola{variable1}")


print(type(print(variable1, variable2, variable3)))  #'NoneType' Because "print" is a function in python

#System Function

print(len(variable1))

#Variables in only one line. Isn't recomendable because this sintaxis could become dangerous
name, surname, alias, age = "Michael", "Portillo", "Raptor", 17
print(name, surname, alias, age)