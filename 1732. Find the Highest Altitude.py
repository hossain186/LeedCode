class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = 0
        new = []

        new.append(n)
        c = 0
        for i in gain:

            c += n+i
            new.append(c)

        return max(new)