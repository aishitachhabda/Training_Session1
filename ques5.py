def product_except_self(arr):
    result = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if i != j:
                prod *= arr[j]
        result.append(prod)
    return result


arr = [1, 2, 3, 4]
print(product_except_self(arr))