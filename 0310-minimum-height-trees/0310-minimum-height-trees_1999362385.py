class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(root: int):
            parent = {root: -1}
            depth = {root: 0}
            stack = [root]
            farthest, max_depth = root, 0
            while stack:
                node = stack.pop()
                if depth[node] > max_depth:
                    max_depth = depth[node]
                    farthest = node
                for nb in adj[node]:
                    if nb not in parent:
                        parent[nb] = node
                        depth[nb] = depth[node] + 1
                        stack.append(nb)
            return farthest, parent
        
        u, _ = dfs(0)
        v, parent = dfs(u)
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        
        L = len(path)
        return [path[L // 2]] if L % 2 else [path[L // 2 - 1], path[L // 2]]