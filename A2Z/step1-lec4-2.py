import sys
class Solution:
    def reverse(self, x: int) -> int:
        if x < (-2**31) or x > ((2**31)-1):
            return 0
        else:
            if x >= 0:
                x = str(x)
                ans = int(x[::-1])
                if ans >= (-2**31) and ans <= ((2**31)-1):
                    return(int(x[::-1]))
                else:
                    return 0
            else:
                x = str(x)
                minus = x[0]
                num = x[1:]
                ans = int(minus + num[::-1])
                if ans >= (-2**31) and ans <= ((2**31)-1):
                    return(int(minus + num[::-1]))
                else:
                    return 0
                    
            
