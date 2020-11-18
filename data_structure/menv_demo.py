from array import array

numbers = array('h', [-2, -1, 0, 1, 2])
menv = memoryview(numbers)
print(menv.tolist())
print(len(menv))
print(menv[0])

menv_oct = menv.cast('B')
print(menv_oct.tolist())

menv_oct[5] = 4
print(numbers)
