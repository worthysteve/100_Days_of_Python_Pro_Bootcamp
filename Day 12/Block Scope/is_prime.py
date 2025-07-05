# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# print(is_prime(2))


def is_prime(number):
    """
    Check if a number is prime.

    A prime number is only divisible by 1 and itself.
    Note: 1 is not considered a prime number.

    Args:
        number: The integer to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases
    if number <= 1:
        return False

    if number == 2:
        return True

    # Check if number is even
    if number % 2 == 0:
        return False

    # Check odd divisors up to the square root of the number
    # We only nesd to check up to the square root because if n = a*b,
    # either a or b must be less than or equal to the square root of n
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

print(is_prime(2))