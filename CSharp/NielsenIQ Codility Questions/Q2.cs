class Solution
{
  public int solution (int D, string S)
  {
    int num = 0;
    switch (S)
      {
      case "one":
	num = 1;
	break;
	case "two":num = 2;
	break;
	case "three":num = 3;
	break;
	case "four":num = 4;
	break;
	case "five":num = 5;
	break;
	default:return 0;
      }
    return D * num;
  }
}




/*
complete following function solution that, given an integer D (between 1 and 5) and a string S (only "one", "two", "three", "four" or "five"), returns the result of multiplying D and S expressed as an integer. For example, given D = 4 and S = "two", your function should return 8.
A) use switch to convert string to number and multiply to get final answer.
*/