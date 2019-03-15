class Solution:
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]

a = [0, 1, 2, 3, 4, 5, 6]
ta = 6

s = Solution()
print(s.twosum(a, ta))