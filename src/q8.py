"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: 3. `n % 2 == 1` is true for odd numbers, so it's counting
    1, 3 and 5 instead of the even ones.

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:      # even = no remainder when divided by 2 (was == 1, which is odd)
            count = count + 1
    return count


if __name__ == "__main__":
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))  # should print 4


"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: It checks if n divided by 2 has no remainder, i.e. n is even.
"""
