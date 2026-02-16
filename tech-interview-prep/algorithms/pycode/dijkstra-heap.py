import heapq


def dijkstra(n, edges, src):
    """
    n: number of nodes labeled [0..n-1]
    edges: adjacency list {u: [(v, w), ...]}
    weights must be non-negative
    Returns: dist list
    """
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]  # (dist, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue  # outdated entry
        for v, w in edges.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist
