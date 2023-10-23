class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def helper(num):
            if num == 1:
                return True
            if num <= 0 or num % 4:
                return False

            return helper(num // 4)

        return helper(n)
        