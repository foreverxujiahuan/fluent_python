needles = {1, 2, 3, 4, 5}
haystack = {2, 3, 6}
# needles在haystack中出现的次数
found = len(needles & haystack)
print(found)
