def sum_even_fibbonaci(up_to):
    first, second = 1, 2
    s = 0
    while first < up_to:
        first, second = second, first+second
        s += first * (first % 2 == 0)
    return s


up_to = 4e6  # Four million
print(sum_even_fibbonaci(up_to))
