import heapq

N = int(input())
L = list(map(int, input().split()))

heapq.heapify(L)

res = 0
while 1 < len(L):
    cost = heapq.heappop(L) + heapq.heappop(L)
    heapq.heappush(L, cost)
    res += cost

print(res)