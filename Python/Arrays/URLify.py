class Solution:
    def URLify(self, s: str):
        s = s.rstrip() # removes trailing spaces
        result = ""
        for char in s:
            if char == " ":
                result += "%20"
            else:
                result += char
        return result

sol = Solution()
print (sol.URLify("Mr John Smith       "))