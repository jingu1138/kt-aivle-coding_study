import heapq
import sys

n = int(sys.stdin.readline())

heap1 = []
heap2 = []
out = []
for _ in range(n):
  x = int(sys.stdin.readline())
  if x > 0:
    heapq.heappush(heap1, x)
  elif x < 0:
    heapq.heappush(heap2, abs(x))
  else:
    if heap1 and heap2:
      pop1 = heapq.heappop(heap1)
      pop2 = heapq.heappop(heap2)
      if pop1 < pop2:
        out.append(pop1)
      else:
        out.append((pop2)*(-1))
    elif 
