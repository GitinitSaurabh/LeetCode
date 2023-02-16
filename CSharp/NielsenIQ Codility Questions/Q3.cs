class Solution {
    public int solution(int[] A) {
        int sum = 0;
        foreach (int num in A) {
            if (num % 4 == 0) {
                sum += num;
            }
        }
        return sum;
    }
}

/* 
Write a function: class Solution { public int solution(int[] A); } that, given an array A consisting of N integers, returns the sum of all integers which are multiples of 4. For example, given array A as follows: [-6, -91, 1011, -100, 84, -22, 0, 1, 473] the function should return -16. Assume that: N is an integer within the range [1..1,000]; each element of array A is an integer within the range [-10,000.. 10,000]; there is at least one element in array A which satisfies the condition in the task statement. 
*/