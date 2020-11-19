#  Brute Force Solution
def largest_palindrome_product(start, end):
    greatest = 0
    for i in range(start, end):
        for j in range(start, end):
            result = i * j
            if is_palindrome(str(result)):
                greatest = max(greatest, result)
    return greatest


#  Generate all 6 digits palindromes and check if they are a product of 2 3-digit numbers
def largest_palindrome_product_2(digits):
    start = 999
    for i in range(0, 899):
        s = str(start-i)
        palindrome = "{}{}".format(s, s[::-1])
        if is_product_3_digits(int(palindrome)):
            return palindrome


def is_product_3_digits(num):
    for i in range(100, 999):
        if num % i == 0 and num/i <= 999:
            return True
    return False


def is_palindrome(str):
    return str == str[::-1]


print(largest_palindrome_product(100, 1000))
print(largest_palindrome_product_2(3))
