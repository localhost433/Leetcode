"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old = {}
        old[node] = Node(node.val)
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in old:
                    old[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old[cur].neighbors.append(old[neighbor])
        return old[node]