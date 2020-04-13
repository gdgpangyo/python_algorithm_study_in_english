# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                max_profit += prices[i] - prices[i-1]

        return max_profit

# test01
solution = Solution()
actual = solution.maxProfit([7,1,5,3,6,4])
expected = 7
print(expected == actual) 

# test02
solution = Solution()
actual = solution.maxProfit([1,2,3,4,5])
expected = 4
print(expected == actual)

# test03
solution = Solution()
actual = solution.maxProfit([7,6,4,3,1])
expected = 0
print(expected == actual)