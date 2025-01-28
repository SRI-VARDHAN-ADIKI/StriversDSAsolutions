class Solution {
  public:
    vector<int> passedBy(int a, int &b) {
        vector<int> ans;
        ans.push_back(a+1);
        ans.push_back(b+2);
        return  ans;
    }
};
