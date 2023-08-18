### Tuples ###

my_tuple = tuple()
my_other_tuple = ("Oh yeah bitches i'm programming in python",)

my_tuple = (35, 1,73, "Michael", "Portillo")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexEror
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Michael"))

print(f"The index is: {my_tuple.index('Michael')}")

#my_tuple[1] = 1.80 #This can't do it because tuples can't be modified
#print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:5])

my_tuple = list(my_tuple)  #this is to make a changeable tuple
print(type(my_tuple))  

my_tuple[4] = "Negro"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[1])
del my_tuple
print(my_tuple)