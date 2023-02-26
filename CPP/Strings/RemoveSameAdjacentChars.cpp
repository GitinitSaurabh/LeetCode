/* 
I/P -> azzayc
O/P -> yc
*/
#include <bits/stdc++.h>
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size();
        std::string new_str;
        for (char c : s) {
            if (isalnum(c)) {
                new_str += c;
            }
        }

        i = 0; 
        j = new_str.size() - 1;
        while(i < j){
            if(tolower(new_str[i]) != tolower(new_str[j])){
                return false;
            }
            j--;
            i++;
        }
        return true;
    }
};