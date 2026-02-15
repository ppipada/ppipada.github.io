class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        best_sum = nums[0]
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum


in_arrs = [
    [2, 1, 2, 1, 0, 1, 2],
    [3, 3, 5, 0, 0, 3, 1, 4],
    [3, 5, 0, 1, 4],
    [1, 2, -1, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
]
if __name__ == "__main__":

    sol = Solution()
    for nin in in_arrs:
        r = sol.maxSubArray(nin)
        print(r)