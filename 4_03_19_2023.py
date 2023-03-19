
# string 
# multiline string :

a = """now i am traying to learn python programming language ,
i already coding practice regular basis , i hope that i complete a small project ."""

print(a)

# strings are arrays :
b = "Hello , World"
print(b[8])

#"for" looping string 

for c in "apple":
    print(c)

#  string leanth :
d = "Hey,Ramesh"
print(len(d))

# check string :
txt = "the best things in my life is happiness"
print("life" in txt) # answer type is bool (boolean) :
print("free" in txt) # answer type is bool (boolean) :

# use it in an "if" statement :
text = "the best things in my life is happiness"
if "happiness" in text :
    print("yes , 'happiness' is present .")

txt1 = "the best things in my life is happiness"
print("free" not in txt1)

txt2 = "the best things in my life is happiness"
if "free" not in txt2 :
    print("No ,'free' is not present in text .")

# Slice string  :

e = "hello , Akash"
print(e[1:])

#  modifying string :

f = "hey , rokey" # Upper Case :

print(f.upper())

g = "HEY , ROKEY" # Lower Case :
print(g.lower())

h = " Hey , Rokey " # any whitespace from the bigining or the end . :
print(h.strip())

i = "Hey Rokey" # Replace Method :
k = i.replace("H","M")
l = k.replace("R","J")
print(l)

j = "Hey Rokey" # Split :
print(j.split("R"))

age = "My name is John, and I am old"
txt = "{} 58"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 4
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 6
itemno = 6235
price = 90.39
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt2 = "We are the so-called \"Vikings\" from the north." # Escape :
print(txt2) 

# python inbuild function :

# capitalize()	Converts the first character to upper case
txt3 = "my name is pritam patra"
n = txt3.capitalize()
print(n)

# casefold()	Converts string into lower case
txt4 = "HeLlo, And Welcome To My World!"

n1 = txt4.casefold()

print(n1)

# center()	Returns a centered string
txt5 = "banana"

n2 = txt5.center(40)

print(n2)


# count()	Returns the number of times a specified value occurs in a string
txt6 = "I love apples, apple are my favorite fruit"

n3 = txt6.count("apple")

print(n3)

# encode()	Returns an encoded version of the string
txt7 = "My name is Ståle"

n4 = txt7.encode()

print(n4)

# endswith()	Returns true if the string ends with the specified value
txt8 = "Hello, welcome to my world ."

n5 = txt8.endswith(".")

print(n5)

# expandtabs()	Sets the tab size of the string
txt9 = "h\te\tl\tl\to"

n6 =  txt9.expandtabs()

print(n6)

# find()	Searches the string for a specified value and returns the position of where it was found
txt10 = "Hello, welcome to my world."

n7 = txt10.find("to")

print(n7)

# format()	Formats specified values in a string
txt11 = "For only {price:.2f} dollars!"
print(txt11.format(price = 50))

# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning