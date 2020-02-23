# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[len(nums)-1]
            for j in range(len(nums)-2, -1, -1):
                nums[j+1] = nums[j]
            nums[0] = temp

        return nums

# test01
solution = Solution()
actual = solution.rotate([1,2,3,4,5,6,7], 3)
expected = [5,6,7,1,2,3,4]
print(expected == actual)

# test02
solution = Solution()
actual = solution.rotate([-1,-100,3,99], 2)
expected = [3,99,-1,-100]
print(expected == actual)

# todo: sovle the time limitation error later
