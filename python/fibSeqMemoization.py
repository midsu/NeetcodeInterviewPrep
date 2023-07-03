# function to generate Fibonacci sequence with memoization
def fibonacci(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        cache[n] = result
        return result

# test the function
for i in range(10):
    print(fibonacci(i))
