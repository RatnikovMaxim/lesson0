def calculate_structure_sum(data_structure):
    get_summa = 0
    if isinstance(data_structure, dict):
        for k, v in data_structure.items():
            get_summa += calculate_structure_sum(k)
            get_summa += calculate_structure_sum(v)
    elif isinstance(data_structure, (list, set, tuple)):
        for i in data_structure:
            get_summa += calculate_structure_sum(i)
    elif isinstance(data_structure, int):
        get_summa += data_structure
    elif isinstance(data_structure, str):
        get_summa += len(data_structure)
    return get_summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
