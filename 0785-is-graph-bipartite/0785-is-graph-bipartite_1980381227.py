class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        s = {}
        for i in range(len(graph)):
            if i not in s:
                stack = [i]
                s[i] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in s:
                            s[neighbor] = 1 - s[node]
                            stack.append(neighbor)
                        elif s[neighbor] == s[node]:
                            return False
        return True