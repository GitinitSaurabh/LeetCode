#include<math.h>
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
         int sum = 0;
         int maxi = INT_MIN;

         for(auto num : nums){
             sum += num;
             maxi = max(maxi, sum);
             sum = sum < 0 ? 0 : sum;
         }
         return maxi;
    }
};