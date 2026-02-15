class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        nlog(n) complexity using sorting. 
        """
        nums.sort()
        l = len(nums)
        start = 0
        end = l - 1
        while start < end:
            s = nums[start] + nums[end]
            if s == target:
                return [start, end]
            if s > target:
                end -= 1
                continue
            start += 1
        return []


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        O(n) complexity using hashmap. 
        """
        m = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in m:
                return [idx, m[complement]]
            m[num] = idx
        return []


if __name__ == "__main__":
    nin = [2, 1, 2, 1, 0, 1, 2]
    tin = 3
    #p = [3,3,5,0,0,3,1,4]
    sol = Solution2()
    r = sol.twoSum(nin, tin)
    print(r)
