n1 = int(input("Enter Number1: "))
n2 = int(input("Enter Number2: "))

for num in range(n1, n2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(f"{num}", end = '  ')