class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] +=1

        sch = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                sch.append(i)
        
        result = []

        while sch:
            cur = sch.popleft()
            result.append(cur)
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    sch.append(next)

        if len(result) != numCourses:
            return []

        return result