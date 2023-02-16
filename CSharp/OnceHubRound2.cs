using System;
using System.Collections.Generic;
using System.Linq;

namespace CheckString {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine(HasSameNumberOfRepeatingCharacters("abcde")); 
            Console.WriteLine(HasSameNumberOfRepeatingCharacters("aabbcc")); 
            Console.WriteLine(HasSameNumberOfRepeatingCharacters("abbbccc")); 
        }

        static bool HasSameNumberOfRepeatingCharacters(string str) {
            Dictionary<char, int> charCounts = new Dictionary<char, int>();
            foreach (char c in str) {
                if (charCounts.ContainsKey(c)) {
                    charCounts[c]++;
                } else {
                    charCounts[c] = 1;
                }
            }
            int count = charCounts.Values.Min();
            int countGreater = 0;
            foreach (int value in charCounts.Values) {
                if (value != count) {
                    countGreater++;
                    if (value != count + 1) {
                        return false;
                    }
                }
            }
            return countGreater <= 1;
        }
    }
}
