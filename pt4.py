mylist = [['aishita','suman','priya','sneha'],[62,60.52],[440022,"yyy"]]


#sorting example 
mylist = [5, 2, 9, 1, 5, 6] 
mylist.sort()
print("Sorted list:", mylist)

day = input("Enter a day of the week: ")

day = day.lower()

if day == "saturday" or day == "sunday":
    print("It is a Weekend")
else:
    print("It is a Working Day")

m1 = int(input("Enter marks of Paper 1: "))
m2 = int(input("Enter marks of Paper 2: "))
m3 = int(input("Enter marks of Paper 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total marks =", total)
print("Average marks =", average)

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))

max = a

if b > max:
    max = b

if c > max:
    max = c

if d > max:
    max = d

if e > max:
    max = e

print("Maximum value is:", max)