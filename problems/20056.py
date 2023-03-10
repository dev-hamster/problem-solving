import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
ans = 0
N, M, K = map(int, input().split())
space = [[deque() for _ in range(N)] for _ in range(N)]
fireballs = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    space[r-1][c-1].append([m, s, d])
    fireballs.append([r-1, c-1])

while K > 0:
    # 파이어볼의 이동
    while fireballs:
        cr, cc = fireballs.popleft()
        m, s, d = space[cr][cc].popleft()
        # 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
        nr = (cr + dy[d] * s) % N 
        nc = (cc + dx[d] * s) % N 
        space[nr][nc].append([m, s, d])

    for cr in range(N):
        for cc in range(N):
            # 한 칸에 두개 이상의 파이어볼
            if len(space[cr][cc]) > 1:
                tmp_m, tmp_s, tmp_d, cnt = 0, 0, [], 0
                odd, even = 0, 0
                while space[cr][cc]:
                    fireball = space[cr][cc].popleft()
                    tmp_m += fireball[0]
                    tmp_s += fireball[1]
                    cnt += 1
                    if fireball[2] % 2 == 0: even += 1
                    else: odd += 1
                tmp_m = tmp_m//5
                # 질량이 0이면 파괴
                if tmp_m == 0: continue
                tmp_s = tmp_s//cnt
                if odd == cnt or even == cnt: tmp_d = [0, 2, 4, 6] 
                else: tmp_d = [1, 3, 5, 7]

                for i in range(4): 
                    fireballs.append([cr, cc])  
                    space[cr][cc].append([tmp_m, tmp_s, tmp_d[i]])
            elif len(space[cr][cc]) == 1: 
                fireballs.append([cr, cc])
    K -= 1

for cr in range(N):
    for cc in range(N):
        ans += sum(arr[0] for arr in space[cr][cc])
print(ans)
