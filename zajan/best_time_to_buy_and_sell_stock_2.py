# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution:
    def maxProfit(self, prices):
        sump = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                sump += prices[i] - prices[i-1]
        return sump


# TestCase
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
