import sys
sys.stdin = open('1003.txt')

def fibonacci(n):

    zero = [1, 0, 1]
    one =[0, 1, 1]

    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f'{zero[n]} {one[n]}')
    

T = int(input())
for _ in range(T):
    N = int(input())
    fibonacci(N)