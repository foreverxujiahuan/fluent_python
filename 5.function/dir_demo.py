def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


dir_list = dir(factorial)
print(dir_list)

a = 'a'
print(dir(a))
