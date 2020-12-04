n = 100
values = range(1, n+1)
print(sum(map(lambda x: x ** 2, values), sum(values) ** 2))
