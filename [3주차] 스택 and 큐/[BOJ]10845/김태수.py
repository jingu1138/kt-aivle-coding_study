from collections import deque
import sys
input = sys.stdin.readline


deq = deque()
n = int(input())
for _ in range(n):
    a = input().split()
    
    if ' ' in a:
        b, c = a.split()
    else:
        b = a
    
    if b == 'push':
        deq.append(c)
    elif b == 'pop':
        if deq:
            print(deq.pop())
        else:
            print('0')
    elif b == 'size':
        print(deq.size())
    elif b == 'empty':
        if deq:
            print('0')
        else:
            print('1')
    elif b == 'front':
        print(deq[len(deq)-1])
    elif b == 'back':
        print(deq[0])
