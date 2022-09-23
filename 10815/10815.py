<<<<<<< HEAD




=======
import sys
sys.stdin = open('10815.txt')

N = int(input())
N1 = list(map(int, input().split()))
M = int(input())
M1 = list(map(int, input().split()))

check = []
N1.sort()  # 첫째 리스트 정렬 이후로는 이진 탐색 알고리즘 그대로

for i in M1:
    start = 0
    end = len(N1)-1
    check = 0

    while start <= end:
        middle = (start + end) // 2

        if N1[middle] == i:
            check = 1
            break

        elif N1[middle] < i:
            start = middle + 1

        else:
            end = middle - 1
    print(check, end=" ")
>>>>>>> 0a007425c5b1211db1f405cab6438924ae83b7b4

