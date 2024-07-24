my_dict = {'Vasya': 1990, 'Masha': 2000, 'Gena': 2005}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'])
print('Not existing value:', my_dict.get('Kolya', 'Такого имени нет'))
my_dict.update({'Yura': 1995,
                'Vanya': 1900})
a = my_dict.pop('Gena')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 4, 'Rom', 'Bar', 3, 4, 'Bar', (12, 34)}
print('Set', my_set)
my_set.update({99999,
               66666666})
print(my_set.remove('Bar'))
print('Modified set:', my_set)
