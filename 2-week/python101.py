#!/bin/python3

#print string

print('Strings and things')
print("Namastey, World!")
print(""" This is multiline String and
We are Here.
        """)
print("This is "+"Strings and things")

#Math

print("Math Time")

print(50+50)
print(50-50)
print(50*50)
print(50/50)
print(50//50)
print(50%50)
print(50**50)

#Variable and Methods

a=20
b=5.2
c="The Sum of"
def sum(a,b):
    return a+b
#formated string literals below
print(f"{c}  {a} and {b} is {sum(a,b)}")
# Type Casting
a=int(b)
b=float(a)
c=str(a)+str(b)
print(f"c={c},  a={a} and b={b}")

#Shorthand Operators
print(f"a={a}")
a+=1
print(f"a={a}")

