#print following patterns

n = 7
for i in range(n):
    for j in range(n):
        if i == 3 or j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("-"*30)

n = 5
for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

print("-"*30)

n = 4
# Upper part
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Lower part
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("-"*30)

n = 5
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


print("-"*30)

n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()