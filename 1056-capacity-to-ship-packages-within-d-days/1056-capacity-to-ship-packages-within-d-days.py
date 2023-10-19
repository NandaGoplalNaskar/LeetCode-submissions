class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        # l, r = 0, float("inf")

        def isPossibleToShip(maxCapacity):
            needDays, curCapacity = 1, 0
            for w in weights:
                curCapacity += w
                if curCapacity > maxCapacity:
                    needDays += 1
                    curCapacity = w
                    if needDays > days: break

            return needDays <= days

        while l < r:
            m = l + (r-l)//2
            if isPossibleToShip(m):
                r = m
            else:
                l = m + 1
        
        return r
        