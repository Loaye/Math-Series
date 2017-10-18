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
