
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

# output variables 
j = "my mother is my life ."
print(j)

k = "my mother"
l = "is"
m = "my life ."

print(k , l , m )

n = "my father"
o = "is"
p = "my heart"

print(n+" "+ o +" "+p)

q = 98
r = 100

print(q + r)

s = "ram"
t = 10
print(s + str(t))

u = "sumi"
v = 10
print(u , v)


# global variable :

y = "good"

def myfun():
  print("SQL is " + y)

myfun()

z = "awesome"

def myfun2():
  z = "fantastic"
  print("python is " + z )

myfun2()

print("py is " + z)

def myfun3():
  global x1
  x1 = "nice"

myfun3()

print("java is " + x1)

x2 = "wow" 

def myfun4():
  global x2
  x2 = "excilent"

myfun4()

print("python is " + x2)

