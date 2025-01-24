class Solution:
    def fib(self, n: int) -> int:
        zeroth, first = 0,1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        for i in range(2,n+1):
            second = zeroth + first
            zeroth = first
            first = second
        
        return second
