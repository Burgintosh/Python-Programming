def big(n):
    k = n
    while True: yield k; k += n
    
print(big(7))