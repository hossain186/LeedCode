class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        new = [str(i) for i in digits]

        total = ""

        for i in new:
            total+=i

        result = str(int(total)+1)

        l = []

        for i in result:
            l.append(int(i))

        return l

