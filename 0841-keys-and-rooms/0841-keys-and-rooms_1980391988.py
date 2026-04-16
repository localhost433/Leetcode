class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = {0}
        stack = [0]
        while stack:
            cur = stack.pop()
            for key in rooms[cur]:
                if key not in visit:
                    stack.append(key)
                    visit.add(key)
        return len(visit) == len(rooms)