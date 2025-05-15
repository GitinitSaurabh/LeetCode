class Solution:
    def PermutationPalindrom(self, input: str) -> bool:
        hash: dict[str, int]  = {}
        answer = True
        counter = 0
        for char in input:
            if char == ' ':
                continue
            char = char.lower()
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1
    
        for count in hash.values():
            if(count % 2 == 1):
                counter += 1
            if(counter > 1):
                answer = False

        return answer
    
sol = Solution()
print(sol.PermutationPalindrom("Tact Coa"))  # True → "taco cat", "atco cta", etc.
print(sol.PermutationPalindrom("hello"))     # False