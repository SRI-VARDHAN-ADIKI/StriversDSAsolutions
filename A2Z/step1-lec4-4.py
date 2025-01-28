
class Solution:
    
        
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        gcd = 1
        for i in range (min(a,b),0,-1):
            
            if a%i == 0 and b%i == 0:
                gcd = i
                break
        else:
            gcd = 1
            
        
        x = []
        lcm = ((a*b)//gcd)
        x.append(lcm)
        x.append(gcd)
        return x
