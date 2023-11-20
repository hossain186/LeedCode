class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        
        a = set(nums)
        
        a = list(a)
        
        new = []
        for i in a:

            c = nums.count(i)
            new.append(c)


        n = max(new)


        for i in a:

            c = nums.count(i)

            if c == n:
                return i