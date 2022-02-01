public class Knapsack{

    public static void Main(){

        int w = 10;
        int n = 4;
        int[] val = {20, 30, 10, 50};
        int[] wt = {1, 3, 4, 6};
        // populating base case
        int[,] dp = new int[n + 1,w + 1];
        for(int r=0; r < w + 1; r++){
            dp[0,r] = 0;
        }
        for(int c=0; c < n + 1; c++){
            dp[c,0] = 0;
        }

        // main logic
        for(int item=1; item<=n; item++){
            for (int capacity = 1; capacity <= w; capacity++)
            {
                int maxValueWithoutCurrentItem = dp[item - 1,capacity];
                int maxValueWithCurrentItem = 0;
                int currentItemWeight = wt[item - 1];
                if(currentItemWeight <= capacity){
                    maxValueWithCurrentItem = val[item - 1];

                    int remainingCapacity = capacity - currentItemWeight;
                    maxValueWithCurrentItem += dp[item - 1,remainingCapacity];
                }
                dp[item,capacity] = Math.Max(maxValueWithoutCurrentItem,maxValueWithCurrentItem);

            }

        }
        Console.WriteLine($"Maximum Value of the Knapsack is: {dp[n,w]}");
    }
}