class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x_str[0] == '-':
            rev = '-' + x_str[len(x_str):0:-1]
        else:
            rev = x_str[::-1]
            
        if int(rev) < -2**31 or int(rev) > 2**31 -1:
            return 0
        else: 
            return int(rev)
        

        
