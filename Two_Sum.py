class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        import sys
        for i in range(1,len(nums)):
            for j in range(len(nums)-1):

                if nums[i]+nums[j] == target:
                    result = [i,j]
                    return result
                    sys.exit()
