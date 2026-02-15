class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return -1
        l = 0
        h = len(height) - 1
        if h < 1:
            return -1
        maxarea = -1
        sidel = h
        while l < h:
            if height[l] < height[h]:
                sidew = height[l]
                l += 1
            else:
                sidew = height[h]
                h -= 1
            a = sidew * sidel
            if a > maxarea:
                maxarea = a
            sidel -= 1
        return maxarea


in_arrs = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1],
    [],
    None,
]

exp_out = [
    49,
    -1,
    -1,
    -1,
]

if __name__ == "__main__":

    sol = Solution()
    for idx, nin in enumerate(in_arrs):
        resout = sol.maxArea(nin)
        print(nin, resout, exp_out[idx], resout == exp_out[idx])