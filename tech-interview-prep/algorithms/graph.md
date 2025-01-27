# Graph Algorithms

## Traversal: Depth First Search

- _Depth First Search_ is a graph traversal algorithm which explores as far as possible along each branch before backtracking
- Time Complexity: `O(|V| + |E|)`

![Alt text](../images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

## Traversal: Breadth First Search

- _Breadth First Search_ is a graph traversal algorithm which explores the neighbor nodes first, before moving to the next level neighbors
- Time Complexity: `O(|V| + |E|)`

![Alt text](../images/dfsbfs.gif?raw=true "DFS / BFS Traversal")

## Topological Sort

- _Topological Sort_ is the linear ordering of a directed graph's nodes such that for every edge from node u to node v, u comes before v in the ordering
- Time Complexity: `O(|V| + |E|)`

## Shortest path: Dijkstra's Algorithm

- _Dijkstra's Algorithm_ is an algorithm for finding the shortest path between nodes in a graph
- Time Complexity: `O(|V|^2)`

![Alt text](../images/dijkstra.gif?raw=true "Dijkstra's")

## Shortest path: Bellman-Ford Algorithm

- _Bellman-Ford Algorithm_ is an algorithm that computes the shortest paths from a single source node to all other nodes in a weighted graph
- Although it is slower than Dijkstra's, it is more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers
- Time Complexity:
  - Best Case: `O(|E|)`
  - Worst Case: `O(|V||E|)`

![Alt text](../images/bellman-ford.gif?raw=true "Bellman-Ford")

## Shortest path: Floyd-Warshall Algorithm

- _Floyd-Warshall Algorithm_ is an algorithm for finding the shortest paths in a weighted graph with positive or negative edge weights, but no negative cycles
- A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between _all_ pairs of nodes
- Time Complexity:
  - Best Case: `O(|V|^3)`
  - Worst Case: `O(|V|^3)`
  - Average Case: `O(|V|^3)`

## MST: Prim's Algorithm

- Minimum Spanning Tree:

  - Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together.
  - A single graph can have many different spanning trees.
  - A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree.
  - The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.

- A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.

- _Prim's Algorithm_ is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. In other words, Prim's find a subset of edges that forms a tree that includes every node in the graph.
  - The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, the other set contains the vertices not yet included.
  - At every step, it considers all the edges that connect the two sets, and picks the minimum weight edge from these edges.
  - After picking the edge, it moves the other endpoint of the edge to the set containing MST.

![Alt text](../images/prim.gif?raw=true "Prim's Algorithm")

- Steps:

  - Create a Min Heap of size V where V is the number of vertices in the given graph. Every node of min heap contains vertex number and key value of the vertex.
  - Initialize Min Heap with first vertex as root (the key value assigned to first vertex is 0). The key value assigned to all other vertices is INF (infinite).
  - While Min Heap is not empty, do following
    - Extract the min value node from Min Heap. Let the extracted vertex be u.
    - For every adjacent vertex v of u, check if v is in Min Heap (not yet included in MST). If v is in Min Heap and its key value is more than weight of u-v, then update the key value of v as weight of u-v.

- Time Complexity: `O(ELogV)`
  - The time complexity of the above code/algorithm looks `O(V^2)` as there are two nested while loops.
  - If we take a closer look, we can observe that the statements in inner loop are executed `O(V+E)` times (similar to BFS).
  - The inner loop has decreaseKey() operation which takes `O(LogV)` time. So overall time complexity is `O(E+V)*O(LogV)` which is `O((E+V)*LogV) = O(ELogV)`

<!-- tabs:start -->

#### **Python**

[Python](../pycode/graph/prims-mst.py ':include :type=code')

<!-- tabs:end -->

## MST: Kruskal's Algorithm

- _Kruskal's Algorithm_ is also a greedy algorithm that finds a minimum spanning tree in a graph. However, in Kruskal's, the graph does not have to be connected

![Alt text](../images/kruskal.gif?raw=true "Kruskal's Algorithm")

- Steps:

  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. Use "Union-Find" for this.
  - Repeat above step until there are (V-1) edges in the spanning tree.

- Time Complexity: `O(ElogE) or O(ElogV)`.
  - Sorting of edges takes `O(ELogE)` time.
  - After sorting, we iterate through all edges and apply find-union algorithm. The find and union operations can take atmost `O(LogV)` time. So overall complexity is `O(ELogE + ELogV)` time.
  - The value of E can be atmost `O(V^2)`, so `O(LogV)` and `O(LogE)` are the same
  - Therefore, overall time complexity is `O(ElogE) or O(ElogV)`

<!-- tabs:start -->

#### **Python**

[Python](../pycode/graph/kruskal-mst.py ':include :type=code')

<!-- tabs:end -->
