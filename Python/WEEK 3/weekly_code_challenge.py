def large_power(base, exponent):
    """Checks if base raised to exponent is greater than 5000."""
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Example:
print(large_power(10, 3))  # True, since 10^3 = 1000 (less than 5000)
print(large_power(20, 3))  # True, since 20^3 = 8000 (greater than 5000)


def divisible_by_ten(num):
    """Checks if num is divisible by 10."""
    if num % 10 == 0:
        return True
    else:
        return False

# Example:
print(divisible_by_ten(50))  # True
print(divisible_by_ten(33))  # False
