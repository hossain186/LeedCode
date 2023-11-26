class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        i = 0
        j = len(s)
        n = len(s)


        result = []
        for k in range(len(s)):

            if s[k] == "I":

                result.append(i)
                i += 1
            else:

                result.append(j)
                j -= 1




        return result+[i]