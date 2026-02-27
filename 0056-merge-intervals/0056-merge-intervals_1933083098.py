class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if next_start <= cur_end:
                cur_end = max(cur_end, next_end)
            else:
                ret.append([cur_start, cur_end])
                cur_start = next_start
                cur_end = next_end
        ret.append([cur_start, cur_end])
        return ret