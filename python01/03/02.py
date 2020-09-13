import functools, operator
m = functools.reduce(operator.add, [1, 2, 3, 4, 5])
n = functools.reduce(operator.add, range(1, 100))
print(m, n)
a = operator.concat("d", "c")
print(a)
