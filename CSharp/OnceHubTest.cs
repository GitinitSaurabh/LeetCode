/*input : abbccdddefghbba
output : defghb
find longest string without repeating character */

public static int LengthOfLongestSubstringWithoutRepeating(string s){

    int n = s.Length();
    int finalAnswer = 0;
    int j = 0;

    Dictionary<char, int> map = new Dictionary<char, int>();

    for(int i=0; i<n; i++){
        if(map.ContainsKey(s[i])){
            j =  Max(j, map[s[i]] + 1); 
        }
        map[s[i]] = i;
        finalAnswer = Max(finalAnswer, i - j + 1);

    }
    return finalAnswer;
}

public static int Max(int a, int b){
    return a > b ? a : b;
}