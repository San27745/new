#5.reverse array
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
rev_arr = arr[::-1]
print("Original Array:", arr)
print("Reverse Array:", rev_arr)