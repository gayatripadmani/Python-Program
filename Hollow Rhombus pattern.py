# hollow and solid rhombus patterns

def hollowRhombus(rows):
    for i in range(1, rows + 1):

        for j in range(1, rows - i + 1):
            print(end=" ")

        if i == 1 or i == rows:
            for j in range(1, rows + 1):
                print("*", end="")

        else:
            for j in range(1, rows + 1):
                if (j == 1 or j == rows):
                    print("*", end="")
                else:
                    print(end=" ")
        print()

def printPattern(rows):
    hollowRhombus(rows)


if __name__ == "__main__":
    rows1 = 5
    rows2 = 8
    rows3 = 3
    printPattern(rows1)
    printPattern(rows2)
    printPattern(rows3)
