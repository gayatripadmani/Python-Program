# write a program to rotate a given matrix 90 degrees in a clockwise direction

def rotate(m):
    if not m or not len(m):
        return

    N = len(m)

    for i in range(N):
        for j in range(i):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp

    for i in range(N):
        for j in range(N // 2):
            temp = m[i][j]
            m[i][j] = m[i][N - j - 1]
            m[i][N - j - 1] = temp


if __name__ == '__main__':

    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    m2 = [
        [11, 22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ]

    rotate(m1)
    rotate(m2)

    for r in m1, m2:
        print(r)
