# Strings

my_string = "My String"
my_other_str = 'My another string'

my_new_line_string = "This is a string\nwith line break"
print(my_new_line_string)

my_tab_string = "\t This is a String with Tab"
print(my_tab_string)

my_scape_string = "\t This is a string \\n scaped" #with double "/" This is to cancel the next function
print(my_scape_string)

# Format #
name, surname, age = "Michael", "Portillo", 17

print(f"My name is {name} {surname} and I'm {age} years old") # First option

print("My name is {} {} and i'm {} years old".format(name, surname, age)) # Secound option

print("My name is %s %s and i'm %d years old" %(name, surname, age)) #Third option

#Character Unpacked
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

#That isn't the same that this
#languaje = "Python"
#a, b = languaje, languaje
#print(a)
#print(b)

#Division
languaje_slice = language[1:3]
print(languaje_slice)

languaje_slice = language[1:]
print(languaje_slice)

languaje_slice = language[-2]
print(languaje_slice)

languaje_slice = language[0:6:2] #This code is for make skips in the string that is to say: from character 0 to 6 make 2 space jumps (0,2,4,6) 
print(languaje_slice)


greeting = "Hello World"

x = greeting [:-3]
y = greeting [-3:]
print(x)
print(y)

#####Reversed#####

reversed_languaje = language[::-1]
print(reversed_languaje)

#Methods
test1 = "Hello world"
print(test1.capitalize())
print(test1.upper())
print(test1.count("o"))
print(test1.lower())
print(test1.isnumeric())
print("7".isnumeric())
print(test1.upper().isupper())
print (len(test1))
print(test1.startswith("He"))
print(test1.endswith("rld"))
print(challenge.expandtabs(20)) #This is not enabled due to that work, the syntax on the variable should be like this: "Hello\tWorld"
