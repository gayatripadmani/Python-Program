def findmissing(a, n):
    temp = [0] * (n + 1)

    for i in range(0, n):
        temp[a[i] - 1] = 1

    for i in range(0, n + 1):
        if (temp[i] == 0):
            ans = i + 1

    print(ans)


# Driver code
if __name__ == '__main__':
    a1 = [3, 6, 1, 5, 4]
    a2 = [8, 3, 2, 1, 5, 4, 7]
    a3 = [3, 2, 4, 5]
    n1 = len(a1)
    n2 = len(a2)
    n3 = len(a3)

    # Function call
    findmissing(a1, n1)
    findmissing(a2, n2)
    findmissing(a3, n3)