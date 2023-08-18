### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [17, 20, 50, 32, 22, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.74, "Michael", "Portillo"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
print(my_other_list.count("Michael")) #This is to count the number of elements that are equal in the list 


age, height, name, surname = my_other_list #Is very probable that it become a error
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] #Is very probable that it become a error
print(name)

print(my_list + my_other_list)

#System Function
print(my_other_list.count("Michael")) #This is to count the number of elements that are equal in the list 

my_other_list.append("Raptor") #This is to add new elements to the list
print(my_other_list)

my_other_list.insert(1, "Negro") #This is to add new elements to the list with the index in this case the element that you inserted the element will only scroll to the next'
print(my_other_list)

my_other_list.remove("Negro") #This function delete the first element you pass to it
print(my_other_list)

print(my_list)
my_list.pop() #This function delete the last element in the list. Also you can delete by index
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] #This is to delete the elements by index and whithout retun like pop
print(my_list)

my_list[1] = 77 #This is to replace elemtes by id
print(my_list)

my_new_list = my_list.copy() #This is to copy the list in THIS POINT

my_list.clear() #Delete all elements in the list
print(my_list)

my_new_list.reverse() # This is for order in backwards
print(my_new_list)

my_new_list.sort() #This is to order by number only with numbers
print(my_new_list)


#Sublistas
print(my_new_list[1:2])


my_list = "Hola mundo"
print(my_list)
print(type(my_list))