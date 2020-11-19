char_id = [('a', 1),
           ('b', 2),
           ('c', 3)]
char2id = {char: i for char, i in char_id}
char2id.update({'d': 4})
print(char2id)
char2id.pop('d')

print(char2id.keys())
print(char2id.values())
