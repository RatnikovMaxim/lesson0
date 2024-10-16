def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            result = text[j:i + j + 1]
            yield result


a = all_variants("abc")
for i in a:
    print(i)
