my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initialValue = 0
while initialValue < len(my_list):
    if my_list[initialValue] < initialValue:
        initialValue += 1
        continue
    else:
        print(my_list[initialValue])
        initialValue += 1