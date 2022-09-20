N = int(input())
rst = 0
for i in range(666, 99999999):
    if '666' in str(i):
        rst += 1
        if rst == N:
            print(i)
            break
