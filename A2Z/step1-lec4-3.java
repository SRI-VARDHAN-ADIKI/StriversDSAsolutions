class Solution {
    public boolean isPalindrome(int x) {
        if(x>=0)
        {
            int sum =0;
            int y = x;
            while(y > 0)
            {
                sum = (sum*10) + (y%10);
                y=y/10;
            }
            if(x == sum)
            {
                return true;
            }
            else
                return false;
        }
        else
            return false;
    }
}
