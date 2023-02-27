class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        
          
        vector<string> ans;
        vector<string> finalAns;
        string s ="";
        int wc = 0;
        int widthLeft = maxWidth; 

        for(int i = 0; i < words.size(); i++){
            if(words[i].size() + wc <= widthLeft){
                ans.push_back(words[i]);
                wc++;
                widthLeft -= words[i].size();
            }
            else{
                i--;
                int sp_bw_words = wc > 1 ? widthLeft : 0;

                int sp_jst = wc == 1 ? widthLeft : 0;

                // adjust spaces between words
                while(sp_bw_words != 0){
                for(int x = 0; x < ans.size() - 1; x++){
                        if(sp_bw_words == 0)
                            break;
                        ans[x].append(" ");
                        sp_bw_words--;
                    }
                }
                
                while(sp_jst != 0){
                for(int x = 0; x <= ans.size() - 1; x++){
                        if(sp_jst == 0)
                            break;
                        ans[x].append(" ");
                        sp_jst--;
                    }
                }
                for(auto word : ans){
                    s += word;
                }
                finalAns.push_back(s);
                ans.clear();
                wc = 0;
                widthLeft = maxWidth;
                s = "";
            }
        }

        // add last line
        for(auto word : ans){
            s += word;
            s += " ";
        }
        s.erase(s.size() - 1);
        while(s.size() < maxWidth){
            s += " ";
        }
        finalAns.push_back(s);

        return finalAns;
        }                 
    };