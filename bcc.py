#python training
print("basic comp coding class day 1")
maths = 40
pi = 3.14
name = 'Aishita'
print(type(maths))
print(type(pi))
print(type(name))


#typecasting
print(2+3)
print("2"+"3")
val1= int(input("enter a number"))
val2= int(input("enter another number"))
print(val1+val2)


print(int(3.14))
print(int(True))
print(int(False))
print(int("45"))

print(float(3.14))
print(float(True))
print(float(False))
print(float("45"))

print(complex(3.14))
print(complex(3))      
print(complex(True))
print(complex(False))
print(complex("45"))
print(complex(3.14))  
print(complex("5.6"))


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", simple_interest)


celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit is:", fahrenheit)

temp = val1
val1 = val2 
val2 = temp
print("After swapping: val1 =", val1, "val2 =", val2)
 
a=20
b=10  
a = a + b 
b = a-b
a = a-b
print("After swapping: a =", a, "b =", b)

num = int(input("Enter a number: "))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

d4 = num % 10
num = num // 10

d5 = num % 10
num = num // 10

d6 = num % 10
num = num // 10

d7 = num % 10
num = num // 10

d8 = num % 10
num = num // 10

d9 = num % 10
num = num // 10

d10 = num % 10

rev = d1*1000000000 + d2*100000000 + d3*10000000 + d4*1000000 + d5*100000 + d6*10000 + d7*1000 + d8*100 + d9*10 + d10

print("Reversed number:", rev)