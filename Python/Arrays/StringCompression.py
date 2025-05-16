class Solution:
    def StringCompression(self, s: str) -> str:
        if not s:
            return ""
        
        hashMap: dict[str, int] = {}
        answer: str = ""
        prevChar = ""
        for char in s:
            if prevChar != "" and char != prevChar:
                answer += prevChar + str(hashMap[prevChar])
                hashMap = {}
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

            prevChar = char
        answer += prevChar + str(hashMap[prevChar])

        return answer if len(answer) < len(s) else s

sol = Solution()
print(sol.StringCompression("AAaaaabbbbccccaaccc"))