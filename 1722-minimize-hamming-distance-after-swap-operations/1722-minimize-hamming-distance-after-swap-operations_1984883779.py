from collections import Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        adj = [[] for _ in range(n)]
        for u, v in allowedSwaps:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                comp = []
                stack = [i]
                visited[i] = True
                
                while stack:
                    cur = stack.pop()
                    comp.append(cur)
                    for neighbor in adj[cur]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                s = Counter()
                for j in comp:
                    s[source[j]] += 1
                for j in comp:
                    if s[target[j]] > 0:
                        s[target[j]] -= 1
                        count += 1
        return n - count
            
