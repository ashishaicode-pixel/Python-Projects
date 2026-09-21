name = ['i', 'a', 'a', 'i', 'e', 'i', 'n',
        'i', 'p', 'o', 'w', 'c', 'x', 'i', 'i']
count = 0
i_word = []
for item in name:
    if item == 'i':
        i_word.append(item)
        count += 1
print(count)
print(i_word)
