class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        comp = [0] * numCourses
        sch = deque([])

        def cycle(v):
            if comp[v] == 1: return True
            if comp[v] == 2: return False
            comp[v] = 1
            for n in adj[v]:
                if cycle(n):
                    return True
            comp[v] = 2
            nonlocal sch
            sch.appendleft(v)
            return False

        for i in range(numCourses):
            if cycle(i):
                return []
        return list(sch)