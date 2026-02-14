class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # adjacent duplicate elements would cause duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # adjacent duplicate elements would cause duplicate triplets
                    # Increment left and right until duplicates are eliminated
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


in_arrs = [
    [-1, 0, 1, 2, -1, -4],
    [1],
    [],
    None,
]

exp_out = [
    set([
        (-1, 0, 1),
        (-1, -1, 2),
    ]),
    set([]),
    set([]),
    set([]),
]

if __name__ == "__main__":

    sol = Solution()
    for idx, nin in enumerate(in_arrs):
        resout = sol.threeSum(nin)
        resout = set(map(tuple, resout))
        di = resout.symmetric_difference(exp_out[idx])
        print(resout, di, False if di else True)
