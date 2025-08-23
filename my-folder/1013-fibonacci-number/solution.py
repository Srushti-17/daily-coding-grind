class Solution:
    def fib(self, n: int) -> int:
        first = 0
        sec = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        for i in range(1,n):
            third = first + sec
            first = sec
            sec = third

        return third    
