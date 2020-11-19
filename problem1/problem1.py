def sum_of_multiples(factors, up_to):
    s = 0
    for i in range(0, up_to):
        for f in factors:
            if i % f == 0:
                s += i
                # To avoid summing up numbers that are multiples of more than 1 factor
                break
    return s


factors = [3, 5]
up_to = 1000
print(sum_of_multiples(factors, up_to))


