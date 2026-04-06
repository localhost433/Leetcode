class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = [False] * n
        def bfs(i):
            queue = deque([i])
            visited[i] = True
            while queue:
                cur = queue.popleft()
                for j in range(n):
                    if isConnected[cur][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)
        return count