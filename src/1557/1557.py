class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = set()

        for from_node, to_node in edges:
            has_incoming.add(to_node)
            
        return [node for node in range(n) if node not in has_incoming]
