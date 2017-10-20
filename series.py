"""Math series to be tested with test_series.py"""

def fib(n):
    """Fibonacci sequence and function"""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def lucas(n):
    """Lucas sequence and function"""
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n + 1)


def sum_series(n, x=0, y=1):
    """sum_series function to find any value in any sequence given"""
    if n == 0:
        return 0
    else:
        series_list = [x, y]
        for i in range(n):
            z = (x + y)
            x = y
            y = z
            series_list.append(z)
        return series_list[n - 1]


if __name__ == "__main__":
    output = """
    This module runs, defines, and implements 3 mathematical function

    fib(n):
    Returns the nth value in the fibonacci series

    >>> fibonacci(2)
    1

    lucas(n):
    Returns the nth value in the lucas series

    >>> lucas(2)
    1

    >>> sum_series(5, 3, 1)
    9
    """


    print("")