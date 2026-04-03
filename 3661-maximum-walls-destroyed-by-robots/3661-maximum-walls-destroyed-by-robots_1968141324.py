from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        tup = sorted(zip(robots, distance))
        walls.sort()

        @cache
        def dfs(i: int, d: str) -> int:
            if i < 0:
                return 0
            
            lb = tup[i][0] - tup[i][1]
            if i > 0:
                lb = max(lb, tup[i-1][0] + 1)
                
            l = bisect_left(walls, lb)
            r = bisect_left(walls, tup[i][0] + 1)
            wl = r - l
            ans = dfs(i-1, 'left') + wl
            
            rb = tup[i][0] + tup[i][1]
            if i + 1 < n:
                if d == 'left':
                    rb = min(rb, tup[i+1][0] - tup[i+1][1] - 1)
                else:
                    rb = min(rb, tup[i+1][0] - 1)
                    
            if rb >= tup[i][0]:
                l = bisect_left(walls, tup[i][0])
                r = bisect_right(walls, rb)
                wr = r - l
            else:
                wr = 0
                
            ans = max(ans, dfs(i-1, 'right') + wr)
            
            return ans
            
        return dfs(n-1, 'right')