# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums):
        dup = {}
        del_idx = []
        for i in range(0, len(nums)):
            exist = self.isExist(dup, nums[i])
            if exist:
                del_idx.append(i)
            else:
                dup[nums[i]] = 1
        cnt = 0
        for i in del_idx:
            del nums[i-cnt]
            cnt+=1
        return len(nums)

    def isExist(self, dup, n):
        for k in dup.keys():
            if k == n:
                return True
        return False

# TestCase
sol = Solution()
nums = [1,1,2]
n = sol.removeDuplicates(nums)

for i in range (0, n):
    print(nums[i])

