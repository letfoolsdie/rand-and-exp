# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    d1 = 1
    d2 = 1
    for i in range(2,n):
        d3 = (d1+d2)%10
        d1 = d2%10
        d2 = d3%10
    return d3

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
