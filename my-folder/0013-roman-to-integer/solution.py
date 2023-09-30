class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000}
        num = 0
        i = 0
        k = 0
        while i < len(s):
            k = i + 1
            if k < len(s) and romans[s[i]] < romans[s[k]]:
                num1 = romans[s[k]] - romans[s[i]]
                num += num1
                i += 2
            else:
                num += romans[s[i]]
                i += 1    
            
        return num
