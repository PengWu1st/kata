
def algo_constant(n):
    """Time: O(1)"""
    print(f"do something for {n}")


def alog_logrithemic(n):
    """Time: O(log(n))
    analysis: 
    0. find k the meet the stop condition, where k is the number of iteration
    1. stop condition: i >= n
    2. f(k) = i: because i *= 2 , i = 1, 2, 4, 8, ..., k , so f(k) = 2^k
    3. solve for k:  2^k >= n => k >= log(n)
    4. time complexity: O(log(n))
    
    """
    i = 1
    while i < n:
        print(f"do something for {i}")
        i *= 2

def algo_root(n):
    """Time: O(sqrt(n))
    analysis:
    0. find k the meet the stop condition, where k is the number of iteration
    1. stop condition: i * i = n
    2. f(k) = i: because i += 1 , i = 1, 2, 3, ..., k , so f(k) = k
    3. solve for k: k * k = n => k = sqrt(n)
    4. time complexity: O(sqrt(n))
    
    """
    i = 1
    while i * i < n:
        print(f"do something for {i}")
        i += 1

def algo_linear_0(n):
    """Time: O(n)"""
    for i in range(n):
        print(f"do something for {i}")

def algo_linear_1(n):
    """Time: O(n)
    step forward or backward doesn't matter
    """
    for i in range(n, 0, -1):
        print(f"do something for {i}")

def algo_linear_2(n):
    """Time: O(n)
    step size doesn't matter
    analysis:
    0. find k the meet the stop condition, where k is the number of iteration
    1. stop condition: i = n
    2. f(k) = i: because i += 2 , i = 0, 2, 4, 6, ..., k , so f(k) = 2k
    3. solve for k:  2k = n => k = n/2
    4. time complexity: O(n/2) = O(n)


    """
    for i in range(0, n, 2):
        print(f"do something for {i}")


def algo_nlogn(n):
    """Time: O(n log(n))
    given loop2 is nested in loop1
    if the time complexity for loop1 is O(a) and loop2 is O(b)
    then time complexity is O(a * b)
    """
    for i in range(n):
        j = 1
        while j < n:
            print(f"do something for {i} and {j}")
            j *= 2


def algo_quadratic(n):
    """Time: O(n^2)"""

    for i in range(n):
        for j in range(n):
            print(f"do something for {i} and {j}")


def algo_cubic(n):
    """Time: O(n^3)"""
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(f"do something for {i}, {j} and {k}")


def algo_exponential(n):
    """Time: O(2^n)"""
    for i in range(2**n):
        print(f"do something for {i}")



