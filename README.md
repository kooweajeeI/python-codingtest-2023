# python-codingtest-2023
파이썬 코딩테스트 리포지토리

## 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - 자료구조 - 배열/리스트
    - 구간 합

## 2일차
! 파이썬 파일명에는 '_'만 사용하자.
1. 코딩테스트 학습
    - 구간 합 2
    - 자료구조
        - 연결리스트
        - 스택
        - pythonds 스택

## 3일차
1. 코딩테스트 학습
    - 자료구조
        - 큐
        - pythonds 큐
        - 이진 트리
            - 삭제는 연결리스트 삭제와 유사
        - 그래프

## 4일차
1. 코딩테스트 학습        
    - 자료구조
        - 그래프 계속
        - 재귀호출
        - 정렬

## 5일차
1. 코딩테스트 학습
    - 자료구조 / 알고리즘
        - 정렬
        - 검색
        - 다이나믹 프로그래밍

## 6일차
1. 코딩테스트 학습
    - 자료구조
        - deque

    - 코딩테스트 알고리즘
        - 백준
        - 프로그래머스

```python
# 백준 2750 - 수 정렬하기
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for i in range(N):
    print(A[i])
```