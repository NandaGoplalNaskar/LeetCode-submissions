class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            n = len(nums1)
            prefix1 = [0] * (n + 1)
            prefix2 = [0] * (n + 1)

            for i in range(1, n+1):
                prefix1[i] = prefix1[i-1] + nums1[i-1]
                prefix2[i] = prefix2[i-1] + nums2[i-1]
            # print(prefix1, prefix2)

            minimum = float("inf")
            ans = 0

            for i in range(1, n + 1):
                curr = prefix2[i] - prefix1[i]
                ans = max(ans, curr - minimum)
                minimum = min(minimum, curr)

            return ans + prefix1[n]

        return max(helper(nums1, nums2), helper(nums2, nums1))