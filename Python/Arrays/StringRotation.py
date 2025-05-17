class Solution:
    def StringRotation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or not s1:
            return False
        return s2.lower() in (s1 + s1).lower()
    
sol = Solution()
print(sol.StringRotation("WaterBottle", "erBottlewat"))