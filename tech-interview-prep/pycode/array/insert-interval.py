class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        s, e = newInterval[0], newInterval[-1]
        left, right = [], []
        for i in intervals:
            if i[-1] < s:
                left += i,
            elif i[0] > e:
                right += i,
            else:
                s = min(s, i[0])
                e = max(e, i[-1])
        return left + [[s, e]] + right