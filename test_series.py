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
    '''Test lucas function to check value of 2'''
    from series import lucas
    assert lucas(2) == 1


def test_lucas_four():
    '''Test lucas function to check value of 4'''
    from series import lucas
    assert lucas(4) == 4


def test_lucas_eight():
    '''Test lucas function to check value of 8'''
    from series import lucas
    assert lucas(8) == 29 


def test_sum_series_zero():
    '''Test sum_series to check value of 0'''
    from series import sum_series
    assert sum_series(0) == 0

def test_sum_series_fib():
    '''Test sum_series to check value of 1 for x and y defaults'''
    from series import sum_series
    assert sum_series(1) == 0

def test_sum_series_lucas():
    '''Test sum_series to check value of eight for x=2 y=1'''
    from series import sum_series
    assert sum_series(8, 2, 1) == 29