cache = {0:0, 1: 1}

# The time complexity is O(log n)
def fib(n):
    print(n)
    print(cache)
    if n < 0:
        print('ERROR')
        return 0

    elif n in cache:
    # else check if the result is in the cache
    # If it is, return the cached result
        return cache[n]
    else:
    # Else, run the calculation and store result in the cache
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

print(fib(100))


# Before caching or `dynamic programming`, extremely slow

# def fib(n):
#     if n < 0:
#         print('ERROR')
#         return 0

#     elif n == 0 or n == 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)