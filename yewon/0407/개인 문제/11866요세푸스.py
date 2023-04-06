# 요세 푸스 문제/ 원형 큐를 구현해보자!
import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int,input().split())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

result = '' # 결과값 출력을 위한 문자열

while queue:
    queue.rotate(-(K-1)) #돌려주기
    result += str(queue.popleft()) + ', '
#형식 맞춰서 출력
print(f'<{result[:-2]}>')
