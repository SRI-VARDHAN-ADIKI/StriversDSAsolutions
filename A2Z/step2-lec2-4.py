class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            partition_index = self.partition(arr, low, high)
            self.quickSort(arr, low, partition_index - 1)
            self.quickSort(arr, partition_index + 1, high)

    def partition(self, arr, low, high):
        pivot_ele = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot_ele and i < high:
                i += 1
            while arr[j] > pivot_ele and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j
