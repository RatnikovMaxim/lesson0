calls = 0


def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    count_calls(1)
    string_list = []
    string_list.append(len(string))
    string_list.append(string.upper())
    string_list.append(string.lower())
    return string_list


def is_contains(string, list_to_search):
    count_calls(1)
    lowercase_list = []
    string.lower()
    for i in list_to_search:
        lowercase_list.append(i.lower())
    return (string.lower() in lowercase_list)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)