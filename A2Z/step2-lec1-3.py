class Solution:
    def insertionSort(self, arr):
        #code here
        for i in range (len(arr)):
            j = i
            
            while (j>0 and arr[j] < arr[j-1]):
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                j-=1
        return arr
