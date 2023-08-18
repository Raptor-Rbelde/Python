### Loops ###


# WHILE
# Syntax
# while condition:
#   code goes here

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:  # Is opcional
    print("My condition is higher than 10")

print("This is out of any loop")

my_condition = 0

while my_condition < 20:
    my_condition += 5
    if my_condition == 15:
        print("My condition is equal to 15 ")
        break
    print("My condition is less than 20")
else:
    print("My condition is higher than 20")

# FOR

my_list = [17, 20, 50, 32, 22, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1,73, "Michael", "Portillo")

my_set = {"Michael", "Portillo", 17}

my_dict = {
    "nombre": "Michael",
    "apellido": "Portillo",
    "edad": 17,
    1: "Python",
    "lenguajes": {"python", "Bash", "Java"}
}

for element in my_tuple:
    print(element)

for element in my_set:
    print(element)

for key in my_dict: # This print the keys
    print(key)


for value in my_dict.values(): 
    print(value)

#Break and Continue
for key in my_dict: # This print the keys
    print(key)
    if key == "edad":
        break
else:
    print("The end of the loop")

for key in my_dict: # This print the keys
    print(key)
    if key == "edad":
        continue  # With this you avoid the next code in the interation and returns you at beginning of the loop
else:
    print("The end of the loop")


#RANGE

lst = list(range(11)) # This is like a for
print(lst) 

# syntax
#for iterator in range(start, end, step):
a = []
for i in range (0,11): # sIs the same that the before script
    a.append(i)
print(a)

#NESTED FOR LOOP

# syntax
# for x in y:
#     for t in x:
#         print(t)