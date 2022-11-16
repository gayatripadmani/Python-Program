def toBinary(n, len):
    binary = ''
    i = 1 << len - 1
    while i > 0:
        binary += '1' if (n & i) else '0'
        i = i // 2
    return binary


if __name__ == '__main__':
    n = 10101
    n1 = 112
    n2 = 29811
    len = 32
    print(f'The binary representation of {n} is', toBinary(n, len))
    print(f'The binary representation of {n1} is', toBinary(n1, len))
    print(f'The binary representation of {n2} is', toBinary(n2, len))