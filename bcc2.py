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