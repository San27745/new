#3.count even and odd
n=int(input("enter length of array"))
print(f'enter {n} integers')
a= [int(input())for _ in range(n)]
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even",even,"odd",odd)