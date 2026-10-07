#1.calculate array sum
num=int(input("enter element"))
a=[]
for i in range(num):
    a.append(int(input("enter element")))
total=sum(a)
print("Sum of array is",total)

print(20*"-")

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
total = 0
for num in arr:
    total = total + num
print("Array:", arr)
print("Sum =", total)



