class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= end:
                end = i.end
            else:
                erased += 1
        return erased