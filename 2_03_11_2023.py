
print("basic variable of python :")

# legal variable name :

myname = "pritam"
my_name = "pritam"
myName = "pritam"
MYNAME = "pritam"
_my_name = "pritam"
myname2 = "pritam"

print(myname) 
print(my_name)
print(myName)
print(MYNAME)
print(_my_name)
print(myname2)

# Multi Words Variable Names :

myDifficultThings = "success" # Camel case (Each word, except the first, starts with a capital letter:)

MyDifficultThings = "success" # Pascal Case (Each word starts with a capital letter:)

my_difficult_things = "success" # Snake Case (Each word is separated by an underscore character:)

print(myDifficultThings)
print(MyDifficultThings)
print(my_difficult_things)

# Many Values to Multiple Variables

a , b , c = "computer" , "keyboard" , "mouse" # assign values to multiple variable in one line :

print(a)
print(b)
print(c)

d = e = f = "cpu" # same value to multiple variable in one line :

print(d)
print(e)
print(f)

ware = ["havels" , "finolex" , "polycape"]  #example of unpack
g , h , i = ware

print(g)
print(h)
print(i)