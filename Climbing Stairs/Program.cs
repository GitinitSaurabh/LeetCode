public class Solution {
    public static int ClimbStairs(int n) {
        
        //declaring dp array
        int[] dp = new int[n+1];

        //possible no. of ways for final two steps is always = 1, so initializing the base case
        //if n = 3
        // 0 1 2 3 
        //     1 1
        dp[n] = 1;
        dp[n-1] = 1;

        //This forms a Fibonacci Sequence
        for(int i= (n-2); i>=0; i--){
            dp[i] = dp[i+1] + dp[i+2];
        }

        //dp[0] will be dp[1] + dp[2] which will be the answer
        return dp[0];
    }
    public static void Main(){
        int stairs = 10;
        Console.WriteLine($"Possible No. of ways are: {ClimbStairs(stairs)}");
    }
}
