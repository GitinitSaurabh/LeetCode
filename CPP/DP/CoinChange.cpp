class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int>dp (amount + 1, -1);
        int ans = recursiveSolve(coins, amount, dp);
        if(ans == INT_MAX){
            return -1;
        }
        else{
            return ans;
        }
    }

    int recursiveSolve(vector<int>& coins, int amount, vector<int>& dp){
            return -1;
        }
        else{
            return ans;
        }
    }

    int recursiveSolve(vector<int>& coins, int amount, vector<int>& dp){

        if(amount == 0){
            return 0;
        }
        if(amount < 0){
            return INT_MAX;
        }
        if(dp[amount] != -1){
            return dp[amount];
        }
        int mini = INT_MAX;

      for(int i=0; i<coins.size(); i++){
      int newAmount = amount - coins[i];
      int ans = recursiveSolve(coins, newAmount, dp);
      if(ans != INT_MAX){
        mini = min(mini, 1 + ans);
      }
      }
      dp[amount] = mini;
      return dp[amount];
    }
};