import io
from pprint import pprint


def custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    line = 0

    for i in strings:
        tell = (file.tell())
        line += 1
        file.write(f'{i}\n')
        strings_positions.update({(line, tell): i})

    file.close()

    return strings_positions


info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
