import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            time, node = heapq.heappop(heap)


            if time > dist[node]:
                continue

            if time >= disappear[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor] and new_time < disappear[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        return [t if t != float('inf') else -1 for t in dist]
