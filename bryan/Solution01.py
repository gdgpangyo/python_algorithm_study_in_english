# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        cur = 0
        for idx in range(len(nums)):
            if (nums[idx] != nums[cur]):
                cur += 1
                nums[cur] = nums[idx]

        return cur + 1

# test01
solution = Solution()
actual = solution.removeDuplicates([1,1,2])
print(actual)

# test02
solution = Solution()
actual = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(actual)
