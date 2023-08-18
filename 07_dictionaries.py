### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_dict = {
    "nombre": "Michael",
    "apellido": "Portillo",
    "edad": 17,
    1: "Python",
    "lenguajes": {"python", "Bash", "Java"}
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))


print(my_dict["nombre"]) # With this you can call the value by means of the key

my_dict["nombre"] = "Xavier" #You can re asing the value 
print(my_dict["nombre"])

print(my_dict[1]) #With this you can call by key and it returns value

my_dict["calle"] = "Calle Raptor" # You can add more elements with this syntax
print(my_dict)

del my_dict["calle"] #This is the form to delete only one element in the dictionary
print(my_dict)

print("Michael" in my_dict)
print("nombre" in my_dict)

print(my_dict.items()) # With this you call group by elements
print(my_dict.keys()) #With this you call the keys that there are in the dictionary
print(my_dict.values()) #With this you call the values that there are in the dictionary


# Playing with "fromkeys" 
# This is to make dictionaries without values 
new_dictionary = dict.fromkeys(("nombre", "apellido", "edad"))
print(new_dictionary)

new_dictionary["nombre"] = "Michael" # Is the same that a normal dictionary
print(new_dictionary)

my_list = ["name", "surname", "age"]
new_dictionary = dict.fromkeys(my_list)
print(new_dictionary)
new_dictionary["name"] = "Michael" 
print(new_dictionary)

my_new_dict = dict.fromkeys(my_dict) # You can do it with a dictionaty
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "BRO")#the shape to set a default text BRO = value
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))