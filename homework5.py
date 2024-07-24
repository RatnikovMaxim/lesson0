immutable_var = (12, 'Rom', [23, 45])
print('immutable_var:', immutable_var)
# immutable_var [1] = True -> TypeError: 'tuple' object does not support item assignment
mutable_list = [23, 'Bar', [56, 78]]
mutable_list [2][1] = True
print('mutable_list:', mutable_list)