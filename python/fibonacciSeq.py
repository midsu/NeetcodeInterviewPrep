def fibonacci(n):
    fib = [0, 1] # initialize list with first two numbers
    while fib[-1] < n: # keep adding numbers until we reach n
        fib.append(fib[-1] + fib[-2])
    return fib[:-1] # return sequence up to but not including n

# example usage
print(fibonacci(10)) # output: [0, 1, 1, 2, 3, 5, 8]
