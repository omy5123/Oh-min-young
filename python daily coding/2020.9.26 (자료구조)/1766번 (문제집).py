import heapq

n, m = map(int, input().split(' '))
num_list = [ [] for _ in range(n+1) ]
indegree = [ 0 for _ in range(n+1) ]
heap = []
result = []

for _ in range(m):
    a, b = map(int, input().split(' '))
    num_list[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    temp = heapq.heappop(heap)
    result.append(temp)
    for i in num_list[temp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

print(" ".join(list(map(str, result))))