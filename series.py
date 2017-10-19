'''Math series to be tested with test_series.py'''

def fib(n):
    '''Fibonacci sequence and function'''
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def lucas(n):
    '''Lucas sequence and function'''
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n + 1)

def sum_series(n, x=0, y=1):
    pass
