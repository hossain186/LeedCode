class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        
        
        new = []
        m = max(candies)
        for i in candies:

            if i+extraCandies>=m:
                new.append(True)
            else:
                new.append(False)

        return new