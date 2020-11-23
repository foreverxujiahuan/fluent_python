s1 = b'caf\xc3\xa9'
res1 = s1.decode('utf-8')
print(res1)

s2 = 'café'
res2 = s2.encode('utf-8')
print(res2)
