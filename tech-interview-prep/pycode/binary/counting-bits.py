class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        offset = 1
        for index in range(1, num + 1):
            if (offset * 2 == index):
                offset *= 2
            result[index] = result[index - offset] + 1
        return result