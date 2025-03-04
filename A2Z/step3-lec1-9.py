class Solution:
    
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):

        a.extend(b)
        
        ans = []
        for i in a:
            if i not in ans:
                ans.append(i)

        ans.sort()
        return ans
# This ans is a brute force approch ,  soon we will come up with an optimal solution
