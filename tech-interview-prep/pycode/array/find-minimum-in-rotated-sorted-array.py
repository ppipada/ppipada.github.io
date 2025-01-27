class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        return self.__fmin(nums, 0, len(nums) - 1)

    def __fmin(self, nums, i, j):
        if i == j:
            return nums[i]
        if i + 1 == j:
            return min(nums[i], nums[j])
        if nums[i] < nums[j]:
            return nums[i]
        mid = int((i + j) / 2)
        if nums[i] < nums[mid]:
            return self.__fmin(nums, mid, j)
        return self.__fmin(nums, i, mid)


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[mid] > nums[hi]):
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


in_arrs = [
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [8, 1, 2, 3],
    [1, 2, 3, 4],
    [1],
    [],
    None,
]

exp_out = [
    1,
    0,
    1,
    1,
    1,
    None,
    None,
]

if __name__ == "__main__":

    sol = Solution()
    sol2 = Solution()
    for idx, nin in enumerate(in_arrs):
        r = sol.findMin(nin)
        print(exp_out[idx] == r, r)
        r = sol2.findMin(nin)
        print(exp_out[idx] == r, r)
