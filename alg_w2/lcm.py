# Uses python3
import sys

#def lcm(a, b):
#    big = max(a,b)
#    i = max(a,b)
#    while True:
#        if big%a==0 and big%b==0:
#            return big
#        else:
#            big+=i
def gcd(a, b):
    if max(a, b)%min(a, b) == 0:
        return min(a, b)
    else:
        return gcd(max(a, b)%min(a, b), min(a,b))
        

def lcm(a, b):
    if max(a,b ) == 0:
        return 1
    else:
        return (a//gcd(a,b)*b)

        


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

