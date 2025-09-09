
## Lab 12: Generators ##

_author_ = "Burgess Doan III"
_credits_ = [""]
_email_ = "doanbs@mail.uc.edu"

# Formatted with Black Formatter
# https://pypi.org/project/black/

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    def __init__(self, word):
        self.word = word

    def __iter__(self):
        for char in self.word:
            yield f"Give me an {char}"
    


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, countdown):
        self.countdown = countdown

    def __iter__(self):
        countdown = self.countdown
        while countdown >= 0:
            yield countdown
            countdown -= 1


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    current = 2
    while True:
        yield current
        current += 2

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]
    """
    for i in s:
        yield i * k

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
    yield 1
    
import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)