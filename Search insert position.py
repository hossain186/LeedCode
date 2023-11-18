class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        result = 0
        for i in range(len(nums)):

            if nums[i]< target:
                result+=1

        return result