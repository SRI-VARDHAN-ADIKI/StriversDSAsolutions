class Solution:
    def sumOfDivisors(self, n):
        #code here 
        som = 0
        for i in range (1,n+1):
           som += (n//i)*i
        
        
        return som
