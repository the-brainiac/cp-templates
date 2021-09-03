def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k]+floyd[k][j])
    
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    # graph = defaultdict(list)
    floyd = [[0 if (i==j) else 10**6 for j in range(n+1)] for i in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        # graph[u].append((v, w))
        floyd[u][v] = w
    
    floyd_warshall()
    for i in range(int(input())):
        a, b = map(int, input().split())
        if floyd[a][b] >= 10**6:
            print(-1)
        else:
            print(floyd[a][b])
