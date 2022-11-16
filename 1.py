n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(i, end=" ")