#7.move zero to end of array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
result = []
zero = 0
for num in arr:
    if num == 0:
        zero = zero + 1
    else:
        result.append(num)
for i in range(zero):
    result.append(0)
print("Original Array:", arr)
print("After moving zeros:", result)