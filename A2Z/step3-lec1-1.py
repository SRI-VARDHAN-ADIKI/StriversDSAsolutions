from typing import List


class Solution:
    def largest(self, arr):
        # code here
        
        maxi = arr[0]
        
        for i in range (len(arr)):
            if maxi < arr[i]:
                maxi = arr[i]
                
        return maxi
