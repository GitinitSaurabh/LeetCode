public class Solution {
    public static int MaxSubArray(int[] nums) {
        if(nums.Length == 1 )
            return nums[0];
        int maxSum = int.MinValue; //For considering case when whole array has negative values only
        int currentSum = 0;
        
        for(int i=0; i<nums.Length;i++){
            currentSum += nums[i];
            if(maxSum < currentSum )
                maxSum = currentSum;
            if(currentSum < 0)
                currentSum = 0;
        }
        return maxSum;

    }
    public static void Main(){
        int [] ex1 = {-2, -3, 3, -1, -2, 1, 5, -3};
        int [] ex2 = {-2,1,-3,4,-1,2,1,-5,4};
        int [] ex3 = {-2,1};
        int [] ex4 = {-2,-1};


;

        Console.WriteLine(MaxSubArray(ex1));
        Console.WriteLine(MaxSubArray(ex2));
        Console.WriteLine(MaxSubArray(ex3));
        Console.WriteLine(MaxSubArray(ex4));
        
    }
}