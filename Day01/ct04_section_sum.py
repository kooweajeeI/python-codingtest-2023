# 입력속도 개선. 단, 주피터노트북에서는 실행불가
import sys
input = sys.stdin.readline      # 이 부분이 없으면 백준 시간초과

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sums = [0]      # 배열 0번째 인덱스
temp = 0

for i in numbers:
    temp += i
    sums.append(temp)

for i in range(M):
    x, y = map(int, input().split())
    print(sums[y] - sums[x-1])
1