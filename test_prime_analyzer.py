"""
Unit Tests for Prime Number Analyzer
------------------------------------
Tests the is_prime and primes_in_range functions using plain assert
statements without any external libraries.
"""

from prime_analyzer import is_prime, primes_in_range


def test_edge_cases_zero_and_one():
    """Test 0 and 1, which are neither prime nor composite."""
    assert is_prime(0) is False, "0 should not be prime"
    assert is_prime(1) is False, "1 should not be prime"
    print("  [PASS] Edge cases: 0 and 1 correctly identified as non-prime")


def test_small_numbers():
    """Test small integers: 2, 3, 4."""
    assert is_prime(2) is True, "2 should be prime (the only even prime)"
    assert is_prime(3) is True, "3 should be prime"
    assert is_prime(4) is False, "4 should not be prime (2 * 2)"
    print("  [PASS] Small numbers: 2 (prime), 3 (prime), 4 (non-prime)")


def test_negative_numbers():
    """Test that negative numbers are not considered prime."""
    assert is_prime(-1) is False, "-1 should not be prime"
    assert is_prime(-2) is False, "-2 should not be prime"
    assert is_prime(-7) is False, "-7 should not be prime"
    assert is_prime(-100) is False, "-100 should not be prime"
    print("  [PASS] Negative numbers correctly identified as non-prime")


def test_large_numbers():
    """Test large prime and large composite numbers."""
    large_prime = 7919  # 1000th prime number
    assert is_prime(large_prime) is True, f"{large_prime} should be prime"

    large_composite_even = 7920
    assert is_prime(large_composite_even) is False, f"{large_composite_even} should not be prime"

    large_composite_odd = 7919 * 3  # 23757
    assert is_prime(large_composite_odd) is False, f"{large_composite_odd} should not be prime"

    perfect_square = 169  # 13 * 13
    assert is_prime(perfect_square) is False, f"{perfect_square} should not be prime"

    print("  [PASS] Large numbers: 7919 (prime), 7920 & 23757 (composite), 169 (square)")


def test_primes_in_range_standard():
    """Test prime generation for a standard range 1 to 20."""
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    actual = primes_in_range(1, 20)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print(f"  [PASS] primes_in_range(1, 20) == {expected}")


def test_primes_in_range_empty():
    """Test prime generation in a range with no prime numbers."""
    # 24, 25, 26, 27, 28 are all composite
    expected = []
    actual = primes_in_range(24, 28)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print("  [PASS] primes_in_range(24, 28) == [] (empty range)")


def test_primes_in_range_inverted():
    """Test inverted range where start > end, ensuring graceful swap."""
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    actual = primes_in_range(20, 1)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print("  [PASS] primes_in_range(20, 1) successfully swapped to [1, 20]")


def test_primes_in_range_negative_and_single():
    """Test ranges containing negative numbers and single-number ranges."""
    # Range spanning negatives and positives
    assert primes_in_range(-10, 5) == [2, 3, 5], "Range from -10 to 5 should yield [2, 3, 5]"
    
    # Single prime range [7, 7]
    assert primes_in_range(7, 7) == [7], "Range [7, 7] should return [7]"

    # Single composite range [8, 8]
    assert primes_in_range(8, 8) == [], "Range [8, 8] should return []"
    print("  [PASS] primes_in_range handles negative ranges and single-value intervals")


def run_all_tests():
    """Run all test functions sequentially."""
    print("=" * 50)
    print("  RUNNING TESTS FOR PRIME NUMBER ANALYZER")
    print("=" * 50)

    test_edge_cases_zero_and_one()
    test_small_numbers()
    test_negative_numbers()
    test_large_numbers()
    test_primes_in_range_standard()
    test_primes_in_range_empty()
    test_primes_in_range_inverted()
    test_primes_in_range_negative_and_single()

    print("=" * 50)
    print("  ALL TESTS PASSED SUCCESSFULLY! (8/8 test suites)")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
