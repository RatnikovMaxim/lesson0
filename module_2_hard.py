n = int(input('Введите число (от 3 до 20): '))


def get_pairs(n):
    number = []
    for i in range(1,21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                number.append(f'{i}{j}')
    # print(f'{number}')
    result = ''.join(number)
    return result


result = get_pairs(n)
print(result)