
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