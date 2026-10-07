#6.remove duplicate from array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print("Original Array:", arr)
print("Array after removing duplicates:", unique)