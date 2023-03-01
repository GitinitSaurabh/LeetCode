#include <vector>
#include <unordered_set>
#include <string>
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
         // Convert the dictionary to a hash set for faster lookup
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());

        // Initialize a table that tracks whether substrings can be segmented
        std::vector<bool> dp(s.size() + 1, false);
        dp[0] = true;

        // Iterate through all possible substrings
        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < i; j++) {
                // Check if the substring s[j:i) can be formed by concatenating a word
                // from the dictionary with another substring that has already been segmented
                if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];