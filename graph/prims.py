from collections import defaultdict, deque
import heapq
import os, sys

def prims(graph, src):
    visited = [False]*(n+1)
    res = 0
    q = []
    heapq.heappush(q, (0, src))
    j = 0
    while j < n:
        wt, vertc = heapq.heappop(q)
        if visited[vertc]:
            continue
        
        res += wt
        visited[vertc] = True
        for i in graph[vertc]:
            b, w = i
            heapq.heappush(q, (w, b))
        j += 1
    return res


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(set)
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].add((v, w))
        graph[v].add((u, w))
    src = int(sys.stdin.readline())
    result = prims(graph, src)
    print(result)
