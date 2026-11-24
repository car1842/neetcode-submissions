class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {

        int n = 0;

        vector<int> ans(2*nums.size());   

        while(n < 2*nums.size()) {

            ans[n] = nums[n % nums.size()];
            n++;

        }
        
        return ans;
    }
};