#1
user_first = input("Enter Your First Name:")
user_last = input("Enter your Last Name:")
print(f"your last name {user_last} Your First Name {user_first} " )
print(f"{user_last} {user_first}")


#1
name = ["neeti", "Sen"]
name.reverse()
print(name)


#2 = Area
import math
r=1.1 #radius
pie = math.pi
print(pie*r*r) #area

#3.
n =  input("Enter a number : ")
print(type(n))

value1 = int(n*2)
print(type(value1))
value2 = int(n*3)
print(type(value2))
value = int(n)+int(value1)+int(value2)
print(f"The Serial of no is {int(n)} + {int(value1)} + {int(value2)}")

print(f"The sum of the Equation is {int(n)} + {int(value1)} + {int(value2)} = {value}")

#4
a = input("Enter a value: ")
val1 = int(a*2)
val2 = int(a*3)
result = (int(a)+int(val1)+int(val2))
print(f'The sum of {int(a)}+{int(val1)}+{int(val2)} = {result}')


#5
a = input("Please input: ")
b = a*2
print(type(a))
print(b)

#6
a = int(input("Enter a no:"))
print(type(a))
b = str(a)*3
print(b)
print(type(b))
