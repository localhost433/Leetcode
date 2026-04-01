class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        result = []
        stack = deque()

        indices.sort(key=lambda x: positions[x])
        for idx in indices:
            if directions[idx] == 'R':
                stack.append(idx)
            else:
                while stack and healths[idx] > 0:
                    right = stack.pop()
                    if healths[right] > healths[idx]:
                        healths[right] -= 1
                        stack.append(right)
                        healths[idx] = 0
                    elif healths[right] < healths[idx]:
                        healths[idx] -= 1
                        healths[right] = 0
                    else:
                        healths[idx] = 0
                        healths[right] = 0
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])
        return result