class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """


        new = {}

        for i in range(len(indices)):

            new[indices[i]] = s[i]

        st = ''

        for i in range(len(indices)):

            st+= new[i]

        return st