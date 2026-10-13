# Prime Number Analyzer

An internship task project (**Level 1, Day 13**) built using only the Python standard library. This project provides an interactive console application to test whether an integer is prime and to discover all prime numbers within a specified range, practicing core concepts such as loops, conditionals, functions, input validation, and algorithmic thinking.

---

## Project Structure

```text
prime-number-analyzer/
├── prime_analyzer.py       # Main program with core functions and interactive CLI
├── test_prime_analyzer.py  # Unit tests using plain assert statements
└── README.md               # Documentation, algorithm explanation & interview Q&A
```

---

## How to Run

### 1. Run the Main Interactive Program
From the project directory, run:
```bash
python prime_analyzer.py
```

### 2. Run the Unit Tests
Execute the tests using standard Python (no external dependencies required):
```bash
python test_prime_analyzer.py
```

---

## Sample Output

### Main Menu & Single Prime Check
```text
============================================
        PRIME NUMBER ANALYZER
============================================
1. Check if a number is prime
2. Generate primes in a range
3. Exit
============================================
Select an option (1-3): 1

--- Check Prime Number ---
Enter an integer to check: 29
Result: 29 IS a prime number.
```

### Checking Composite Number (with Educational Feedback)
```text
Select an option (1-3): 1

--- Check Prime Number ---
Enter an integer to check: 49
Result: 49 is NOT a prime number (divisible by 7).
```

### Input Validation (Graceful Recovery)
```text
Select an option (1-3): 1

--- Check Prime Number ---
Enter an integer to check: abc
  [!] Invalid input: Please enter a valid integer (e.g., -5, 0, 17).
Enter an integer to check: 7919
Result: 7919 IS a prime number.
```

### Generating Primes in a Range
```text
Select an option (1-3): 2

--- Generate Primes in a Range ---
Enter start of range: 1
Enter end of range: 20

Primes in range [1, 20]:
  Found 8 prime(s):
  [2, 3, 5, 7, 11, 13, 17, 19]
```

### Handling Inverted Range (start > end)
```text
Select an option (1-3): 2

--- Generate Primes in a Range ---
Enter start of range: 25
Enter end of range: 10
  Note: Start (25) is greater than End (10). Swapping to range [10, 25].

Primes in range [10, 25]:
  Found 5 prime(s):
  [11, 13, 17, 19, 23]
```

### Unit Test Execution Output
```text
==================================================
  RUNNING TESTS FOR PRIME NUMBER ANALYZER
==================================================
  [PASS] Edge cases: 0 and 1 correctly identified as non-prime
  [PASS] Small numbers: 2 (prime), 3 (prime), 4 (non-prime)
  [PASS] Negative numbers correctly identified as non-prime
  [PASS] Large numbers: 7919 (prime), 7920 & 23757 (composite), 169 (square)
  [PASS] primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
  [PASS] primes_in_range(24, 28) == [] (empty range)
  [PASS] primes_in_range(20, 1) successfully swapped to [1, 20]
  [PASS] primes_in_range handles negative ranges and single-value intervals
==================================================
  ALL TESTS PASSED SUCCESSFULLY! (8/8 test suites)
==================================================
```

---

## Algorithm Explanation

### What is a Prime Number?
A **prime number** is a natural number strictly greater than 1 ($n > 1$) whose only positive divisors are 1 and the number itself.
- Examples of primes: $2, 3, 5, 7, 11, 13, 17, 19, 23, \dots$
- Numbers $\le 1$ (such as negative numbers, 0, and 1) are **not** prime by definition.
- A composite number is a positive integer greater than 1 that has at least one divisor other than 1 and itself.

### Why Checking Divisors Only Up to $\sqrt{n}$ is Enough
Any factor of a number $n$ comes as part of a factor pair $(a, b)$ such that:
$$a \times b = n$$

If both factors $a$ and $b$ were greater than $\sqrt{n}$, their product would be:
$$a \times b > \sqrt{n} \times \sqrt{n} = n$$
which is impossible. Therefore, in every factor pair $(a, b)$, at least one of the factors must be less than or equal to $\sqrt{n}$ ($a \le \sqrt{n}$), while the other must be greater than or equal to $\sqrt{n}$ ($b \ge \sqrt{n}$).

If we test all potential divisors from $2$ up to $\lfloor\sqrt{n}\rfloor$ and find no number that divides $n$, then $n$ cannot have any divisors larger than $\sqrt{n}$ either. Thus, $n$ is guaranteed to be prime.

### Why Even Numbers Are Skipped
- The number $2$ is the smallest and only even prime number.
- Any even number greater than $2$ is by definition divisible by $2$ ($n = 2 \times k$ where $k > 1$), making it composite.
- By checking if $n$ is divisible by $2$ once at the start, we eliminate half of all possible numbers.
- Subsequent divisor checks can start at $3$ and increment by $2$ ($3, 5, 7, 9, \dots$), testing only odd candidates and cutting the loop iterations in half.

### Time & Space Complexity Analysis
- **Single Number Primality Test (`is_prime(n)`):**
  - **Time Complexity:** $O(\sqrt{n})$. In the worst case (when $n$ is prime), the loop runs up to $\frac{\sqrt{n}}{2}$ times. In Big-O notation, constant factors are dropped, giving $O(\sqrt{n})$.
  - **Space Complexity:** $O(1)$ auxiliary space, since only a few scalar variables (`limit`, `divisor`) are allocated.
- **Range Prime Generation (`primes_in_range(start, end)`):**
  - For a range of $m$ integers ($m = \text{end} - \text{start} + 1$) up to maximum value $n = \text{end}$:
  - **Time Complexity:** Roughly $O(m \cdot \sqrt{n})$ in the worst case, as each candidate number is checked with `is_prime`.
  - **Space Complexity:** $O(k)$ where $k$ is the number of primes found in the range (at most $m$), required to store the resulting list.

---

## Interview Questions & Answers

### 1. What is a prime number?
A prime number is an integer greater than 1 that cannot be formed by multiplying two smaller positive integers. It has exactly two distinct positive divisors: 1 and itself.
- $0$ and $1$ are not prime numbers.
- Negative numbers are not prime numbers.
- $2$ is the only even prime number (all other even numbers are multiples of 2).

### 2. How can the prime-checking algorithm be optimized?
1. **Square Root Limit ($\sqrt{n}$):** Instead of checking all numbers up to $n - 1$ ($O(n)$) or $n / 2$, limit checks to $\lfloor\sqrt{n}\rfloor$ ($O(\sqrt{n})$).
2. **Skipping Even Numbers:** Check divisibility by 2 first, then only check odd numbers ($3, 5, 7, \dots$), cutting search space by 50%.
3. **Wheel Factorization ($6k \pm 1$):** All primes greater than 3 can be expressed in the form $6k \pm 1$ ($6k - 1$ or $6k + 1$). Testing only divisors of this form reduces the number of checks by about 66% compared to trial division by all numbers.
4. **Sieve of Eratosthenes (for Ranges):**
   - When generating all prime numbers up to a large number $N$, checking each number individually with trial division takes $O(N\sqrt{N})$.
   - The **Sieve of Eratosthenes** pre-allocates a boolean array of size $N$ and iteratively marks multiples of each prime starting from $p^2$ as composite.
   - It runs in $O(N \log \log N)$ time, which is vastly faster than individual checks for large limits.

### 3. What is algorithm complexity?
Algorithm complexity is a formal measure of how the resource requirements of an algorithm scale with the size of its input ($n$):
- **Time Complexity:** The amount of computational time (or number of elementary operations) an algorithm takes as input size grows.
- **Space Complexity:** The amount of memory (RAM/storage) an algorithm requires beyond the input itself.
- **Big-O Notation ($O$):** Expresses the theoretical upper bound (worst-case scenario) of an algorithm's growth rate, ignoring hardware differences and constant multipliers (e.g., $O(1)$ constant time, $O(\log n)$ logarithmic time, $O(n)$ linear time, $O(\sqrt{n})$ sub-linear time, $O(n^2)$ quadratic time).
- **Practical Significance:** Understanding complexity helps engineers select the most scalable and efficient algorithm for their system constraints (e.g., avoiding exponential or quadratic slowdowns on large datasets).
