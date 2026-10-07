#2.find smallest and largest element 
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
arr.sort()
print("Array:", arr)
print("Smallest =", arr[0])
print("Second Smallest =", arr[1])
print("Largest =", arr[-1])
print("Second Largest =", arr[-2])
        



























# #cube sum of n natural numbers
# n=int(input("enter number"))
# sum=(n*(n+1)//2)**2
# print(sum)
