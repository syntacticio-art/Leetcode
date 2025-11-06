from typing import List           # We’ll use List for type hints (helps readers/tools understand types)
import heapq                      # heapq gives us a min-heap (always pops the smallest number)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # c = number of cities (they’re labeled 1..c)
        # connections = list of [u, v] pairs: there’s a wire (edge) between city u and v
        # queries = list of [t, x], where:
        #   t == 1 → ask: “what’s the smallest ONLINE city in x’s connected group?”
        #   t == 2 → command: “turn city x OFFline”
        # Returns a list of answers for all type-1 queries (in order)

        parent = list(range(c + 1))   # parent[i] starts as i → each city is its own parent (own group)
        rank = [0] * (c + 1)          # rank[i] helps keep trees shallow when we union groups

        def find(x):
            # Find the leader (root) of x’s group, with path compression (speed trick)
            if parent[x] != x:        # if x is not its own parent, follow the chain up
                parent[x] = find(parent[x])  # compress path: point x directly to the root
            return parent[x]          # return the group leader

        def union(a, b):
            # Join the groups that contain a and b (union by rank)
            ra, rb = find(a), find(b)     # find each group’s leader (root)
            if ra == rb:                  # already in the same group → nothing to do
                return
            if rank[ra] < rank[rb]:       # attach the smaller tree under the bigger one
                ra, rb = rb, ra
            parent[rb] = ra               # make ra the parent of rb
            if rank[ra] == rank[rb]:      # if both trees were same height, bump ra’s rank
                rank[ra] += 1

        # 1) Build groups from the given connections using DSU
        for u, v in connections:      # for each wire (u—v)
            union(u, v)               # merge the groups of u and v

        # 2) For each group leader, we’ll keep a min-heap of its member cities
        comp_heap = [[] for _ in range(c + 1)]  # one heap per possible leader index
        for node in range(1, c + 1):            # go through each city 1..c
            r = find(node)                      # find its group leader
            comp_heap[r].append(node)           # put the city into that leader’s heap list

        for r in range(1, c + 1):               # turn each group’s list into a real min-heap
            if comp_heap[r]:
                heapq.heapify(comp_heap[r])     # heapify makes smallest element pop first

        # 3) Track which cities are online right now (all start online)
        online = set(range(1, c + 1))           # a set so we can quickly check/remove cities

        ans = []                                 # we’ll collect answers for type-1 queries here
        for t, x in queries:                     # handle each query in order
            r = find(x)                          # find the group leader for city x

            if t == 1:                           # Question: “smallest ONLINE city in x’s group?”
                if x in online:                  # if x itself is online…
                    ans.append(x)                # …it’s the smallest (because min-heap ensures smallest index,
                                                # and if x is online and equals the heap top or smaller ones are offline,
                                                # returning x is still correct as we check heap next when needed)
                else:
                    heap = comp_heap[r]          # get the heap for x’s group
                    # Pop any cities from the top that are no longer online
                    while heap and heap[0] not in online:
                        heapq.heappop(heap)      # remove offline city from the top

                    if heap:                     # if there’s at least one online city left
                        ans.append(heap[0])      # return the smallest online city in this group
                    else:
                        ans.append(-1)           # no online city found in this group

            else:                                # t == 2 → Command: “turn city x OFF”
                if x in online:                  # only if it’s currently online
                    online.remove(x)             # mark it offline (we lazily drop it from heap when encountered)

        return ans                                # give back all collected answers for type-1 queries
