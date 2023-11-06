class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
    
        b = nums[0:n]
        c = nums[n:]
        new = []

        for i in range(len(b)):
            new.append(b[i])
            new.append(c[i])


        return new