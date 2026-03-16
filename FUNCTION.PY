def add(): 
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    sum = n1 + n2
    mul = n1*n2
    sub = n1-n2
    div = n1/n2
    return sum, mul, sub, div   
result = add()
print(result)