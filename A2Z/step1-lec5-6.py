#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        #code here 
        ans = []
        product = 1
        i = 2
        while (product <= n):
            ans.append(product)
            product *= i
            i+=1
            
        return ans
        

