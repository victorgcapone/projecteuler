#  Brute Force Solution
def largest_palindrome_product(start, end):
    greatest = 0
    for i in range(start, end):
        for j in range(start, end):
            result = i * j
            if is_palindrome(str(result)):
                greatest = max(greatest, result)
    return greatest


def is_palindrome(string):
    return string == string[::-1]


print(largest_palindrome_product(100, 1000))
