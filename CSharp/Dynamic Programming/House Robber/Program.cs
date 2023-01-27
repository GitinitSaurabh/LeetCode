public class Solution {

    public static void Main(){
        int[] val = {2,7,9,3,1};
        Console.WriteLine($"Max money is: {Rob(val)}");
    }
    public static int Rob(int[] nums) {
        
        int big = Int32.MinValue;
        
        for(int i=0;i<nums.Length;i++){
            for(int j=i+2;j<nums.Length;j++){
                big = Math.Max(nums[i]+nums[j], big);
            }
        }
        
        return big;
    }
    
}