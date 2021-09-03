import math 
from collections import Counter, defaultdict, deque
import sys
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)

"""
# Template Designed By: Shivshanker Singh
# Note: If you find this template useful and want to use it then please don't just copy paste it 
		you can take ideas from this and make your own.
		because if you copy paste as it is then there are high chances that both of us will be plagiarized
		(because most of code will be same for small problems).
		So to avoid this please dont copy paste.
"""

mod       = 10**9 + 7
input     = sys.stdin.readline
readInt   = lambda : int(input().strip())
readfloat = lambda : float(input().strip())
readStr   = lambda : input().strip()
intList   = lambda : list(map(int, input().strip().split()))
intMap    = lambda : map(int, input().strip().split())
floatList = lambda : list(map(float, input().strip().split()))
floatMap  = lambda : map(float, input().strip().split())
strList   = lambda : list(input().strip().split())


def print(*args, end='\n', sep=' '):
	for i in args:
		sys.stdout.write(str(i))
		sys.stdout.write(sep)
	sys.stdout.write(end)


def bfs(cur):
    visited[cur] = 1
    res[cur] = 0

    q = deque()
    q.append(cur)
    while len(q):
        current = q.popleft()
        for child in graph[current]:
            if child != current:
                q.append(child)
                if child == n:
                    res2.add(res[current]+1)
                res[child] = min(res[child],res[current] + 1)
                visited[child] = 1
    
if __name__ == '__main__':
#for _ in range(readInt()):
    n, m, t, c = intMap()
    graph = defaultdict(list)
    for i in range(m):
        u, v = intMap()
        graph[u].append(v)
        graph[v].append(u)
    res = [n]*1001
    visited = [0]*1001
    res2 = set()
    bfs(1)
    # print(res2)
    if len(res2) == 1:
        print(-1)
    else:
        min_bridge = sorted(res2)[1]
        time = 0
        for i in range(min_bridge):
            if time%(2*t) > t:
                time += (t-time%t)
            time += c

        print(time)
        # print(solve())