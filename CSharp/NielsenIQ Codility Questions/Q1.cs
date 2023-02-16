using System;
using System.Text;
					
public class Program
{
	public static string solution(int N) {
    // create the base string "+--"
    string baseStr = "+--";
    // create a StringBuilder to build the final string
    StringBuilder sb = new StringBuilder(N);
    // iterate over the characters of the base string, appending them to the final string
    for (int i = 0; i < N; i++) {
        sb.Append(baseStr[i % 3]);
    }
    // return the final string
    return sb.ToString();
}
	public static void Main()
	{
		Console.WriteLine(solution(5));
	}
}

/*
We consider a string which is created by repeating the string "+--". Write a function solution that, given an integer N, returns the first N characters of this string. You can assume N is between 1 and 200. Examples: 1. Given N = 5, the function should return "+--+-". 2. Given N = 7, the function should return "+--+--+”.
*/