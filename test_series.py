'''Test for math series.'''

def test_fib_zero():
    '''Test fib function to check value 0 of fibonacci'''
    from series import fib
    assert fib(0) == 0

def test_fib_one():
    '''Test fib function to check value 1 of fibonacci'''
    from series import fib
    assert fib(1) == 0

def test_fib_two():
    '''Test fib function to check value 2 of fibonacci'''
    from series import fib
    assert fib(2) == 1

def test_fib_five():
    '''Test fib function to check value 5 of fibonacci'''
    from series import fib
    assert fib(5) == 3

def test_fib_seven():
    '''Test fib function to check value 7 of fibonacci'''
    from series import fib
    assert fib(7) == 8


def test_lucas_zero():
    '''Test lucas function to check value of 0'''
    from series import lucas
    assert lucas(0) == 0

def test_lucas_one():
    '''Test lucas function to check value of 1'''
    from series import lucas
    assert lucas(1) == 2

def test_lucas_two():
    '''Test lucas function to check value of 0'''
    from series import lucas
    assert lucas(2) == 1