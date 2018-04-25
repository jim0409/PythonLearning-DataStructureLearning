class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # set an index to record step
        # meet an non-zero value in nums store it, else ommit
        k = 0
        for num in nums:
            if num!=0:
                nums[k]=num
                k+=1
        # relpace the k+1 index corresponding value with zero
        nums[k:]=[0]*(len(nums)-k)