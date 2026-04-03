class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        comp = [0] * numCourses

        def cycle(v):
            if comp[v] == 1: return True
            if comp[v] == 2: return False
            comp[v] = 1
            for n in adj[v]:
                if cycle(n):
                    return True
            comp[v] = 2
            return False

        for i in range(numCourses):
            if cycle(i):
                return False
        return True