


class Solution {
    public int getSecondLargest(int[] arr) {
        int largest = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }

        int secondL = Integer.MIN_VALUE;

        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > secondL && arr[i] != largest) {
                secondL = arr[i];
            }
        }

        if (secondL != Integer.MIN_VALUE)
        {
            return secondL;
        }
        else
        {
            return -1;
        }
    }
}
