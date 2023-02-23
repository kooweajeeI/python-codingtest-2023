# 백준 1991 - 트리 순회
import sys
input = sys.stdin.readline

N = int(input())
tree = {} # 딕셔너리

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preOrder(now):
    if now == '.':
        return
    print(now, end='')      # 현재노드
    preOrder(tree[now][0])  # 왼쪽탐색
    preOrder(tree[now][1])  # 오른쪽탐색

def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])  # 왼쪽탐색
    print(now, end='')      # 현재노드
    inOrder(tree[now][1])  # 오른쪽탐색

def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])  # 왼쪽탐색
    postOrder(tree[now][1])  # 오른쪽탐색  
    print(now, end='')      # 현재노드

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
