class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.   
    def frequencyCount(self, arr):
        #  code here
        
        # pre-computation
        has = [0 for i in range (len(arr)+1)]
        for i in range (len(arr)):
            has[arr[i]] += 1
            
        return has[1:]
