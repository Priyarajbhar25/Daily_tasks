
def fibonacci_series(limit):
    fib = [0, 1]  # Starting values of the Fibonacci series
    while True:
        next_fib = fib[-1] + fib[-2]  # Sum of the last two numbers
        if next_fib > limit:
            break
        fib.append(next_fib)
    return fib
limit = 50
fib_series = fibonacci_series(limit)
print("Fibonacci series between 0 and ",limit,fib_series)
