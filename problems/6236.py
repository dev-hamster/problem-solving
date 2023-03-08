import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = list(map(int, input().split()))

l = max(money)
r = sum(money) 
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    cur_money = 0

    for x in money:
        if cur_money >= x:
            cur_money -= x
        else:
            cur_money = mid
            cur_money -= x
            cnt += 1    

    if cnt > M:
        l = mid+1
    else:
        r = mid-1
print(l)