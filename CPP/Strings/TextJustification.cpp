public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> result;
    int n = words.size();
    int i = 0;
    while (i < n) {
        int j = i + 1;
        int len = words[i].size();
        while (j < n && len + 1 + words[j].size() <= maxWidth) {
            len += 1 + words[j].size();
            j++;
        }
        int spaces = maxWidth - len;
        int num_words = j - i;
        if (num_words == 1 || j == n) {
            // left-justified or last line
            string line = words[i];
            for (int k = i + 1; k < j; k++) {
                line += " " + words[k];
            }
            line += string(maxWidth - len, ' ');
            result.push_back(line);
        } else {
            // fully justified
            int space_per_word = spaces / (num_words - 1);
            int extra_spaces = spaces % (num_words - 1);
            string line = words[i];
            for (int k = i + 1; k < j; k++) {
                line += string(space_per_word, ' ');
                if (extra_spaces > 0) {
                    line += " ";
                    extra_spaces--;
                }
                line += " " + words[k];
            }
            result.push_back(line);
        }
        i = j;
    }
    return result;