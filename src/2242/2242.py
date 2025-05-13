class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        top_neighbors = [[] for _ in range(n)]
        for u in range(n):
            neighbors = graph[u]
            top_neighbors[u] = sorted(neighbors, key=lambda x: -scores[x])[:3]

        max_score = -1

        for u, v in edges:
            for a in top_neighbors[u]:
                if a == v:
                    continue
                for b in top_neighbors[v]:
                    if b == u or b == a:
                        continue
                    max_score = max(max_score, scores[a] + scores[u] + scores[v] + scores[b])

        return max_score