class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}
        for n in nums:
            if n in h:
                return True
            h[n] = True
        return False


class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False


in_arrs = [
    [2, 1, 2, 1, 0, 1, 2],
    [3, 3, 5, 0, 0, 3, 1, 4],
    [3, 5, 0, 1, 4],
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]
if __name__ == "__main__":

    sol = Solution2()
    for nin in in_arrs:
        r = sol.containsDuplicate(nin)
        print(r)
