### Sets ###


# Definition
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #It said that is a dictionary

my_other_set = {"Michael", "Portillo", 17}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Raptor")
print(my_other_set) # A set is not an order structure

my_other_set.add("Raptor") # In a set you can't repeat elements

print(my_other_set)

print("Michael" in my_other_set)
print("Raptoor" in my_other_set)

my_other_set.remove("Raptor")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set #NameError: name 'my_other_set' is not defined



my_set = {"Michael", "Portillo", 17}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Pyhon", "R", "Bash"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"JavaScript"})) #This ignore the repeats and only add the new elements

print(my_new_set.difference(my_set)) #Because with this you delete the union between my_set and my_new_set and no "javascript" appears because is not in an variable only is in the print
