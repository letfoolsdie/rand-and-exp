# Uses python3
#def calc_fib(n):
#    if (n <= 1):
#        return n
#
#    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    d1 = 1
    d2 = 1
    for i in range(2,n):
        d3 = d1+d2
        d1 = d2
        d2 = d3
    return d3

n = int(input())

print(calc_fib(n))
