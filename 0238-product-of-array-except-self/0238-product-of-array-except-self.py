class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_of_nums = len(nums)
        pre, post = 1, 1
        ans = [1] * length_of_nums

        for i in range(length_of_nums):
            ans[i] = ans[i] * pre
            pre = pre * nums[i]
            ans[length_of_nums - i - 1] *= post
            post = post * nums[length_of_nums - i - 1]

        return ans
        