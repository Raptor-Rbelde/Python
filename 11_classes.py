### Classes ###

# Method = is a behavior of an object like: walk, sing, bark, etc
# Method = Is a function that is defined inside a class
# Attribut = is a characteristics of an object like: name, age, color, etc

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = ""):
        self.__name = name          #Private property
        self.surname = surname      #Public Property
        self.full_name = f"{name} {surname} {alias}"
    
    def get_name (self):
        return self.__name
    
    def walk (self):    # This is a method
##       print(f"{self.full_name} is walking")
        return f"{self.full_name} is walking"



my_person = Person("Michael", "Portillo") # We create an objecct by calling the class
print (my_person.get_name())
print(my_person.full_name)
## my_person.walk()
print(my_person.walk())

my_other_person = Person("Michael", "Portillo", "Raptor")
print(my_other_person.walk())
my_other_person.full_name = "Holaaa" # You can change the value inside off variable because the class constructur is mutable
print(my_other_person.full_name)
