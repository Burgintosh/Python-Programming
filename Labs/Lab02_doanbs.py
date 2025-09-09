# CS2021 Lab 02 - Required Questions
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
## you can then submit you program for credit. 

_author_ = "Burgess Doan III"
_credits_ = [""]
_email_ = "doanbs@mail.uc.edu" # Your email address

#  RQ1
"""
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is 'Sunday'. 
Your function should return error message if the arguments to the function are not valid. 
"""
def day_name(n):
    """
    >>> day_name(3) 
    'Wednesday'
    >>> day_name(6) 
    'Saturday'
    >>> day_name(42)
    'Invalid argument'
    """
    
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if(not (n < 7 and n >= 0) ):
        return "Invalid argument"
    return week[n]

#  RQ2
def two_of_three(a, b, c):
    """Return value using only a one-line return statement.  The value should be the sum of two squares x*x + y*y, 
         where x and y are the two largest members of the set of. positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    arr = [a,b,c]
    max = 0
    second_max = 0
    for i in arr:
        if(i > max):
            max = i
    for i in arr:
        if(i < max and i > second_max):
            second_max = i
    if second_max == 0:
        second_max = max
    return ((max*max) + (second_max*second_max))
        


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    increment = 1
    max_factor = 0
    while increment < n:
        if n % increment == 0:
            max_factor = increment
        increment+=1
    return max_factor
                 

# RQ 4
def keeper(pred, n):
    """Print the numbers between 1 and n which satisfy the predicate pred.

    >>> keeper(lambda x: x%2 == 0, 15)
    2 4 6 8 10 12 14 
    >>> keeper(lambda x: x%7 == 0, 40)
    7 14 21 28 35 
    """
    
    x = 1
    while x <= n: 
        if(pred(x)):
            print(x, end=" ")
        x+=1
        
          
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)