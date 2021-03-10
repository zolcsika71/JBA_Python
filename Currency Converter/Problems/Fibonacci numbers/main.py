def fib(n):

    if n == 0:    # base case n=0
        return 0
    elif n == 1:  # base case n=1
        return 1
    else:
        # case n>1
        return fib(n - 1) + fib(n - 2)
