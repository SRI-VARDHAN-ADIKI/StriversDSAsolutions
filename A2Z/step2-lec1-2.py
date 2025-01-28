
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,a):
        # code here
        for i in range(len(a)-1):
            for j in range (len(a)-1):
                if a[j] > a[j+1]:
                    temp = a[j] 
                    a[j] = a[j+1]
                    a[j+1] =temp
        return a
