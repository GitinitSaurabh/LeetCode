public class Solution {
    public static void Main(){
        int numRows = 6;
        foreach (var item in Generate(numRows))
        {
            foreach (var finalItem in item)
            {
                Console.Write(finalItem + " ");
            }
            Console.WriteLine();

        }
    }
    public static IList<IList<int>> Generate(int numRows) {
        
        IList<IList<int>> res = new List<IList<int>>();
        IList<int> prev = new List<int>();
        IList<int> curr = new List<int>();
        
        for(int i=0;i<numRows;i++){
            curr = new List<int>();
            for(int j=0;j<=i;j++){
                if(i==j || j==0)
                    curr.Add(1);
                else
                    curr.Add(prev[j-1] + prev[j]);
            }
            prev = curr;
            res.Add(curr);
        }
        return res;
        
    }
}