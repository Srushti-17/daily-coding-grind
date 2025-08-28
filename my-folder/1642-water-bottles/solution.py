class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles
        curr = numBottles

        while curr >= numExchange:
            new = curr // numExchange
            cnt += new
            curr = new + (curr % numExchange)

        return cnt
        
