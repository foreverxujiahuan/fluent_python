def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(42))

print(type(factorial))

print(factorial.__doc__)

fact = factorial
print(fact(5))

print(map(factorial, range(11)))

print(list(map(factorial, range(11))))
