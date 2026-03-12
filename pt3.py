mylist =["aishita","suman","priya","sneha",62,60.52]
newlist = mylist.copy() #clonning a list    
print(mylist)
print(newlist)
del list
print(list)

m1 = int(input("Enter marks of Paper 1: "))
m2 = int(input("Enter marks of Paper 2: "))
m3 = int(input("Enter marks of Paper 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total marks =", total)
print("Average marks =", average)