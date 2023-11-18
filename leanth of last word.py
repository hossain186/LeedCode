class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """


        n  = s.strip()
        new = n.split(" ")

        return len(new[-1])

        