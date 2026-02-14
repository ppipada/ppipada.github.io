class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.__search(nums, 0, len(nums) - 1, target)

    def __binsearch(self, nums, i, j, target):
        if i == j:
            if nums[i] == target:
                return i
            return -1

        if i + 1 == j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            return -1

        mid = int((i + j) / 2)
        if nums[mid] < target:
            return self.__binsearch(nums, mid, j, target)
        return self.__binsearch(nums, i, mid, target)

    def __search(self, nums, i, j, target):
        if i == j:
            if nums[i] == target:
                return i
            return -1

        if i + 1 == j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            return -1

        if nums[i] < nums[j]:
            return self.__binsearch(nums, i, j, target)

        mid = int((i + j) / 2)
        if nums[i] < nums[mid]:
            if (target <= nums[mid]) and (target >= nums[i]):
                return self.__binsearch(nums, i, mid, target)
            return self.__search(nums, mid, j, target)
        if (target >= nums[mid]) and (target <= nums[j]):
            return self.__binsearch(nums, mid, j, target)
        return self.__search(nums, i, mid, target)


class Solution2(object):
    def find_min_index(self, nums):
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
        return lo

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        rot_index = self.find_min_index(nums)
        hi = len(nums) - 1
        if rot_index == 0:
            return self.__binsearch(nums, rot_index, hi, target)
        if target >= nums[rot_index] and target <= nums[hi]:
            return self.__binsearch(nums, rot_index, hi, target)
        return self.__binsearch(nums, 0, rot_index - 1, target)

    def __binsearch(self, nums, i, j, target):
        if i > j:
            return -1
        if i == j:
            if nums[i] == target:
                return i
            return -1

        if i + 1 == j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            return -1

        mid = int((i + j) / 2)
        if nums[mid] < target:
            return self.__binsearch(nums, mid, j, target)
        return self.__binsearch(nums, i, mid, target)


in_arrs = [
    ([3, 4, 5, 1, 2], 4),
    ([4, 5, 6, 7, 0, 1, 2], 1),
    ([8, 1, 2, 3], 3),
    ([1, 2, 3, 4], 5),
    ([1], 1),
    ([], 1),
    (None, 1),
    ([5, 1, 3, 4], 5),
    ([8, 1, 2, 3], 1),
    ([1, 2, 3, 4], 4),
    ([1, 2, 3, 4], 1),
    ([1], 0),
]

exp_out = [
    1,
    5,
    3,
    -1,
    0,
    -1,
    -1,
    0,
    1,
    3,
    0,
    -1,
]

if __name__ == "__main__":

    sol = Solution()
    sol2 = Solution()
    for idx, nin in enumerate(in_arrs):
        r = sol.search(nin[0], nin[1])
        print(exp_out[idx] == r, r)
        r = sol2.search(nin[0], nin[1])
        print(exp_out[idx] == r, r)
