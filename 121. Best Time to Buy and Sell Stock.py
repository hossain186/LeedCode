class Solution(object):
    def maxProfit(self, prices):

        buy = 0
        sell = 1
        result = 0
        while sell< len(prices):

            profit = prices[sell] - prices[buy]
            
            if prices[sell]>prices[buy]:
                result  = max(result, profit)
            else:

                buy = sell

            sell +=1


        return  result

