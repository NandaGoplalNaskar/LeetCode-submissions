class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums1 = set(nums)
        nums = list(nums1)
        nums.sort()
        # print(nums)
        n = len(nums)
        pre = [1]*n

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                pre[i] += pre[i-1]

        # print(pre)

        if n > 0:
            return max(pre)
        else:
            return 0

