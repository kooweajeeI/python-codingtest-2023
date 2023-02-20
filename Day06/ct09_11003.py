# 백준 11003 - 최솟값찾기 1

from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

# 새 값이 들어올 때 마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거
# 시간복잡도를 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재 값보다 크면
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L:  # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end = ' ')     # 무조건 최소값(min()과 동일)