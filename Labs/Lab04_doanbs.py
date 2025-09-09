##Lab04 Required Questions ##

#########
# Lists #
#########

_author_ = "Burgess Doan III"
_credits_ = [""]
_email_ = "doanbs@mail.uc.edu"

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    """forward = []
    backward = []
    i = 0
    while i < len(lst):
        forward += [lst[i]]
        backward = [lst[i]] + backward
        i += 1
    return forward + backward"""
    return lst + lst[::-1]
        

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    for j in range(2):
        for i in range(len(seq)):
            seq[i] = fn(seq[i])
    return seq

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    for i in seq:
        if(pred(i)):
            seq.remove(i)
    return seq

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x % 2 == 0)
    [0, 2, 4, 6]
    """
    return [x for x in range(n) if pred(x)]
        

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    new_list = []
    for i in range(len(lst)):
        if(type(lst[i]) == list):
            new_list += flatten(lst[i])
        else:
            new_list += [lst[i]]
    return new_list
        
            
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)