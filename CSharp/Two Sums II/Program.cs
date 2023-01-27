public class Solution {
    public  static int[] TwoSum(int[] numbers, int target) {
        IDictionary<int,int> dic = new Dictionary<int,int>(); // Will use Reverse dictionary Value:Key instead of Key:Value
        int i1=0,i2=0;
        for(int i=0;i<numbers.Length;i++)
        {
            int diff;
            diff = target - numbers[i];
            if(dic.ContainsKey(diff))
            {
                i1 = i;
                i2 = dic[diff];
            }
            else
            {
                // dic.Add(i,numbers[i]);
                dic[numbers[i]]=i; //Can't use .Add() in reverse dictionary(Value:Key) as Values are not unique
                //Hence we replace previous repeating Value with new Value. 
            }
        }
        return new int[]{i2+1,i1+1};
        
    }
    public static void Main(){
        int[] ex1 = {2,7,11,15};
        Console.WriteLine(TwoSum(ex1,9));
    }
}