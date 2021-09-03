from collections import defaultdict, deque
import heapq
import os, sys

def dijkstra(graph, src):
    dist = [10**6]*(n+1)
    visited = [False]*(n+1)
    dist[src] = 0
    q = []
    heapq.heappush(q, (0, src))
    while q:
        vertc = heapq.heappop(q)[1]
        if visited[vertc]:
            continue
        visited[vertc] = True
        for i in graph[vertc]:
            b, w = i
            if dist[vertc] + w < dist[b]:
                dist[b] = dist[vertc] + w
                # q.append((-dist[b], b))
                heapq.heappush(q, (dist[b], b))
    
    res = []
    for i in range(1, n+1):
        if i != src:
            if dist[i] >= 10**6:
                res.append(-1)
            else:
                res.append(dist[i])
    return res


for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(set)
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].add((v, w))
        graph[v].add((u, w))
    src = int(sys.stdin.readline())
    result = dijkstra(graph, src)
    print(*result)
