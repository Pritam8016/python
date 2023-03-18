# data type :
# 1. str type
a = "twentyfive"
print(type(a))
 
# numeric type

b = 25
print(type(b))
      
c = 25.5
print(type(c))

d = 25j 
print(type(d))  # display the data type of d :

e = ["apple" , "banana" , "mango"]
print(type(e))

f = ("apple" , "banana" , "mango")
print(type(f))

i = range(6)
print(i)
print(type(i))

j = {"name" : "pritam" , "age" : "27"}
print(j)
print(type(j))

k = {"pritam" , "swapan" , "chandana"}
print(k)
print(type(k))

l = frozenset({"pritam" , "swapan" , "chandana"})
print(l)
print(type(l))

m = True
print(m)
print(type(m))

n = b"hello"
print(n)
print(type(n))

o = bytearray(6)
print(o)
print(type(o))

p = memoryview(bytes(6))
print(p)
print(type(p))

q = None
print(type(q))

# python number : int , float , complex .
# flaot
r = 5e3
s = 5E3
t = -5.3e1

print(r)
print(s)
print(t)

# random

import random
print(random.randrange(2, 20))

