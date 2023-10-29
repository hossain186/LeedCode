class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        a  = strs
        _min = len(min(a,key=len))
        print(_min)
        result = ''

        for i in range(_min):

            s = [word[i] for word in a]

            print(s)
            if len(set(s)) == 1:
                result+= s[0]
            else:
                break

        return result

