class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        best = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        for x in range(1, len(nums)):
            n = (nums[x], nums[x] * current_max, nums[x] * current_min)
            current_max = max(n)
            current_min = min(n)
            best = max(current_max, best)
            print(nums[x], current_max, current_min, best)
        return best


in_arrs = [
    # [2, 1, 2, 1, 0, 1, 2],
    # [3, 3, 5, 0, 0, 3, 1, 4],
    # [3, 5, 0, 1, 4],
    # [1, 2, -1, 1],
    # [1, 2, 3, 4],
    # [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [2, 3, -2, 4],
    [-2, 0, -1],
    [-2],
    [-4, -3],
    [-2, 3, -4],
    [2, -3, 4],
    [0, -2, -3],
    [0, -2],
    [2, -3, 4, 0],
    [2, -5, -2, -4, 3],
]

if __name__ == "__main__":

    sol = Solution()
    for nin in in_arrs:
        print(nin)
        r = sol.maxProduct(nin)
        print(r)