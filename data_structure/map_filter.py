symbols = "!@#$%%^&"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 10]
beyond_ascii_by_map = list(filter(lambda c: c > 10, map(ord, symbols)))
print(beyond_ascii)
print(beyond_ascii_by_map)
