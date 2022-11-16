import math

PRIME_NUMBERS = []


def is_monisen_number(value):
    log2 = int(math.log2(value + 1))
    return 2**log2 == value + 1 and log2 in PRIME_NUMBERS


def is_prime_number(value):
    stop_guard = int(math.sqrt(value))
    for p_num in PRIME_NUMBERS:
        if value % p_num == 0:
            break
        elif p_num > stop_guard:  # prime found
            return True
    else:
        return True
    return False


def get_monisen_numbers(count):
    start = 2
    monisen_numbers = []

    while True:
        if len(monisen_numbers) == count:
            return monisen_numbers

        if is_prime_number(start):
            PRIME_NUMBERS.append(start)
            if is_monisen_number(start):
                monisen_numbers.append(start)
        start += 1


if __name__ == '__main__':
    count = int(input('Please input the {n}th number (n > 6 would cost very long time): '))
    print(get_monisen_numbers(count))