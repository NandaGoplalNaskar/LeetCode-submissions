import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # Create a defaultdict to store the graph
        graph = defaultdict(list)

        # Populate the graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Dictionary to store the shortest distance
        shortest = {}

        # Priority queue (min heap) to process nodes
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # Check if all nodes are reachable
        if len(shortest) != n:
            return -1

        # Find the maximum shortest distance
        return max(shortest.values())
