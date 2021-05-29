# OUT

+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
<!---->
## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def canFinish(self, numCourses, prerequisites):
    graph = dict()
    for k, it in groupby(sorted(prerequisites), key=lambda x: x[0]):
        graph[k] = {e for _, e in it}
    sub_graph = {}
    while True:
        vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
        sub_graph = {k: vertex_set & vs for k, vs in graph.items()
             if k in vertex_set and vertex_set & vs}
        if sub_graph == graph:
            break
        else:
            graph = sub_graph
    if graph:
        return False
    return True
    print("Есть цикл!" if graph else "Нет цикла.")
def findOrder(self, numCourses, prerequisites):
    if not self.canFinish(numCourses, prerequisites):
        return []
    num_heads = defaultdict(int)   # num arrows pointing in
    tails = defaultdict(list)      # list of arrows going out
    heads = []                     # unique list of heads in order first seen
    for h, t in prerequisites:
        num_heads[t] += 1
        if h in tails:
            tails[h].append(t)
        else:
            tails[h] = [t]
            heads.append(h)
    ordered = [h for h in heads if h not in num_heads]
    for h in ordered:
        for t in tails[h]:
            num_heads[t] -= 1
            if not num_heads[t]:
                ordered.append(t)
    cyclic = [n for n, heads in num_heads.items() if heads]
    for i in range(numCourses):
        if i not in ordered:
            ordered.append(i)
    return reversed(ordered)

```

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
def canFinish(self, numCourses, prerequisites):
    graph = dict()
    for k, it in groupby(sorted(prerequisites), key=lambda x: x[0]):
        graph[k] = {e for _, e in it}
    sub_graph = {}
    while True:
        vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
        sub_graph = {k: vertex_set & vs for k, vs in graph.items()
             if k in vertex_set and vertex_set & vs}
        if sub_graph == graph:
            break
        else:
            graph = sub_graph
    if graph:
        return False
    return True

```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def numIslands(self, grid):
    islands_num = 0
    heigth = len(grid)
    width = len(grid[0])
    def dfs(i, j):
        grid[i][j] = 0
        if j > 0 and grid[i][j-1] == "1":
            dfs(i, j-1)
        if j < width-1 and grid[i][j+1] == "1":
            dfs(i, j+1)
        if i < heigth-1 and grid[i+1][j] == "1":
            dfs(i+1, j)
        if i > 0 and grid[i-1][j] == "1":
            dfs(i-1, j)
    for i in range(heigth):
        for j in range(width):
            if (grid[i][j] == "1"):
                islands_num += 1
                dfs(i, j)
    return islands_num

```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
 color = defaultdict(int)
 def dfs(cur):
  for neighbor in graph[cur]:
   if neighbor in color:
    if color[cur] == color[neighbor]:
	    return False
   else:
    color[neighbor] = ~color[cur]
    if not dfs(neighbor):
	    return False
  return True
 for node, _ in enumerate(graph):
  if not dfs(node):
   return False
 return True
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n, flights, src, dst, k):
    pq, g = [(0,src,k+1)], collections.defaultdict(dict)
    for s,d,w in flights:
        g[s][d] = w
    while pq:
        cost, s, k = heapq.heappop(pq)
        if s == dst:
            return cost
        if not k: continue
        for d in g[s]:
            heapq.heappush(pq, (cost+g[s][d], d, k-1))
    return -1
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
def shortestPathBinaryMatrix(self, grid):
    rows = len(grid)
    cols = len(grid[0])
    if grid[0][0] == 1:
        return -1
    q = [(0, 0, 1)]
    while len(q) > 0:
        x, y, d = q.pop(0)
        if x == rows-1 and y == cols-1:
            return d
        for a, b in ((x-1, y-1), (x+1, y+1), (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y+1), (x+1, y-1)):
            if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 0:
                grid[a][b] = 1
                q.append((a, b, d+1))
    return -1
```

