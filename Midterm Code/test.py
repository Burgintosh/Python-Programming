print(max([-2, -1, 0, 1], key=lambda x: x*x)) # -2
def factorial(n):
    if n == 0: # Base case
        return 1
    else:
        return n * factorial(n-1) # Recursive case
    
def fib(n):
    if n <= 1: # Base case
        return 1
    else:
        return fib(n-1) + fib(n-2) # Recursive case
    
def xxx(n): 
    if n == 0: print(0, end = ' ')
    else: xxx(n-1); print(n, end = ' ') 
    # xxx(5) output