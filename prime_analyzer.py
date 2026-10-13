"""
Prime Number Analyzer
---------------------
An internship project (Level 1, Day 13) demonstrating loops, conditions,
functions, input validation, and basic algorithmic thinking.

This program provides tools to:
1. Check whether a single integer is prime using an optimized O(sqrt(n)) algorithm.
2. Generate all prime numbers within a specified range [start, end].
"""

import math


def is_prime(n: int) -> bool:
    """
    Check if a given integer n is a prime number.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Optimization steps:
    1. Numbers <= 1 (including all negatives, 0, and 1) are not prime.
    2. 2 is the smallest and only even prime number.
    3. Any other even number (n > 2 and n % 2 == 0) is composite.
    4. Only odd divisors from 3 up to sqrt(n) need to be tested. If n had a
       divisor greater than sqrt(n), its paired cofactor would be smaller
       than sqrt(n), which would have already been detected.

    Args:
        n (int): The integer to evaluate.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    # 0, 1, and negative numbers cannot be prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Any other even number is not prime
    if n % 2 == 0:
        return False

    # Test odd divisors from 3 up to floor(sqrt(n))
    # Step by 2 to check only odd candidates (3, 5, 7, 9, ...)
    limit = math.isqrt(n)
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False  # Early exit as soon as a factor is found

    return True


def primes_in_range(start: int, end: int) -> list[int]:
    """
    Generate all prime numbers in the inclusive range [start, end].

    If start > end, the bounds are automatically swapped to ensure
    a valid range traversal.

    Args:
        start (int): The starting integer of the range.
        end (int): The ending integer of the range.

    Returns:
        list[int]: A list containing all prime numbers between start and end.
    """
    # Handle inverted ranges gracefully by swapping
    if start > end:
        start, end = end, start

    # Collect primes using the reusable is_prime function
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes


def get_integer_input(prompt: str) -> int:
    """
    Prompt the user for an integer with robust input validation.

    Keeps prompting until the user enters a valid integer, preventing
    program crashes from ValueError.

    Args:
        prompt (str): The prompt message displayed to the user.

    Returns:
        int: The validated integer entered by the user.
    """
    while True:
        raw_input = input(prompt).strip()
        try:
            return int(raw_input)
        except ValueError:
            print("  [!] Invalid input: Please enter a valid integer (e.g., -5, 0, 17).")


def handle_check_prime() -> None:
    """Handle menu option 1: Check if a single number is prime."""
    print("\n--- Check Prime Number ---")
    number = get_integer_input("Enter an integer to check: ")

    if is_prime(number):
        print(f"Result: {number} IS a prime number.")
    else:
        # Provide helpful context for why it's not prime
        if number <= 1:
            print(f"Result: {number} is NOT a prime number (primes must be greater than 1).")
        elif number % 2 == 0 and number > 2:
            print(f"Result: {number} is NOT a prime number (even number divisible by 2).")
        else:
            # Find the smallest factor for educational feedback
            limit = math.isqrt(number)
            smallest_factor = next((d for d in range(3, limit + 1, 2) if number % d == 0), None)
            if smallest_factor:
                print(f"Result: {number} is NOT a prime number (divisible by {smallest_factor}).")
            else:
                print(f"Result: {number} is NOT a prime number.")


def handle_primes_in_range() -> None:
    """Handle menu option 2: Generate primes in a given range."""
    print("\n--- Generate Primes in a Range ---")
    start = get_integer_input("Enter start of range: ")
    end = get_integer_input("Enter end of range: ")

    if start > end:
        print(f"  Note: Start ({start}) is greater than End ({end}). Swapping to range [{end}, {start}].")

    actual_start, actual_end = min(start, end), max(start, end)
    primes = primes_in_range(start, end)

    print(f"\nPrimes in range [{actual_start}, {actual_end}]:")
    if primes:
        print(f"  Found {len(primes)} prime(s):")
        print(f"  {primes}")
    else:
        print("  No prime numbers found in this range.")


def main() -> None:
    """Main program loop offering an interactive menu-driven interface."""
    while True:
        print("\n" + "=" * 44)
        print("        PRIME NUMBER ANALYZER")
        print("=" * 44)
        print("1. Check if a number is prime")
        print("2. Generate primes in a range")
        print("3. Exit")
        print("=" * 44)

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            handle_check_prime()
        elif choice == "2":
            handle_primes_in_range()
        elif choice == "3":
            print("\nThank you for using Prime Number Analyzer. Goodbye!")
            break
        else:
            print("  [!] Invalid choice: Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
