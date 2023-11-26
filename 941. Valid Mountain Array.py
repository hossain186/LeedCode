class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        maxi = max(arr)
        ind = arr.index(maxi)
        if len(arr) == 2:
            return False
        if ind == 0 or ind == (len(arr) - 1):
            return False
        for i in range(ind, len(arr) - 1):

            if arr[i] > arr[i + 1]:
                continue
            else:
                return False

        for i in range(ind):

            if arr[i] < arr[i + 1]:
                continue
            else:
                return False
        return True