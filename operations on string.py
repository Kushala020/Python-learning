#strip()
s1="python "
print(s1.strip())

print("python"=="python ")
print("python"==s1.strip())

#replace
s1="i am kushala"
print(s1.replace("kushala","kushi"))


#counting substring from a string
s1="python is fun.i am learning python.python always"
s2="us"
print(s1.count(s2))

#changing case of a string
#1 upper()
s1="kushala is a student"
print(s1.upper())
#2 lower()
print(s1.lower())
#3 title()
print(s1.title())
#4 capitalise()
print(s1.capitalize())

#starting and ending of a string
s1="java"
print(s1.startswith("J"))
print(s1.startswith("j"))