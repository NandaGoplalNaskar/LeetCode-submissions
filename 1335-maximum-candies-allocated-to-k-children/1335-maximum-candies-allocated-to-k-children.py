class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        s = sum(candies)
        if s < k: return 0
        l, r = 1, s//k

        def helper(p):
            return sum(c//p for c in candies) >= k

        while l < r:
            mid = (l+r+1)//2 
            if helper(mid):
                l = mid
            else:
                r = mid - 1

        return l
        