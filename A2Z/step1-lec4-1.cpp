class Solution{
public:
    int evenlyDivides(int n){
        //code here
        int k = n;
        int sum = 0;
        while(n>0)
        {
            if ((n%10 != 0) &&(k%(n%10))==0)
            {
                sum ++;
            }
            n = n/10;
        }
        return sum;
    }
};
