# 백준 11657 - 타임머신

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

edges = []
distance = [sys.maxsize]*(N+1)

for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0

for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

mCycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True       # 음수사이클이 존재!
        break       # 음수사이클이 있으면 더이상 진행할 필요없음

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)

else:
    print(-1)
