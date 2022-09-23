

def fibonnaci(n):
    def fib(n, dp_results):
        if n <= 1:
            return n

        if dp_results[n] != -1:
            return dp_results[n]

        dp_results[n] = fib(n-1, dp_results) + fib(n-2, dp_results)
        return dp_results[n]

    dp_results = [-1] * (n+1)
    return fib(n, dp_results)


print(fibonnaci(5))
    
