from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        for u, v in connections:
            union(u, v)

        comp_heap = [[] for _ in range(c + 1)]
        for node in range(1, c + 1):
            r = find(node)
            comp_heap[r].append(node)

        for r in range(1, c + 1):
            if comp_heap[r]:
                heapq.heapify(comp_heap[r])

        online = set(range(1, c + 1))

        ans = []
        for t, x in queries:
            r = find(x)

            if t == 1: 
                if x in online:
                    ans.append(x)
                else:
                    heap = comp_heap[r]
                    while heap and heap[0] not in online:
                        heapq.heappop(heap)
                    if heap:
                        ans.append(heap[0])
                    else:
                        ans.append(-1)

            else:  
                if x in online:
                    online.remove(x)

        return ans
