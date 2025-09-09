_author_ = "Burgess Doan III"
_credits_ = ["""
            https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions
            https://www.reddit.com/r/learnpython/comments/lqkh53/overflowerror_integer_division_result_too_large/
            https://docs.python.org/3/library/decimal.html
            """]
_email_ = "doanbs@mail.uc.edu"

import math
from decimal import *

'p = integer 1 (numerator) | q = integer 2 (denominator)'
def egypt(p, q):
    """
    >>> egypt(3,4)
    '1/2 + 1/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12'
    >>> egypt(6,7)
    '1/2 + 1/3 + 1/42'
    >>> egypt(5,8)
    '1/2 + 1/8'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """
    
    if(p == 0 or q == 0):
        return "None"
    denom = math.ceil(Decimal(q)/Decimal(p))
    to_return = "1/" + str(denom)
    next_loop = egypt((p * denom - q), (q * denom))
    if(next_loop != "None"):
        to_return = to_return + " + " + next_loop
    return to_return

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)