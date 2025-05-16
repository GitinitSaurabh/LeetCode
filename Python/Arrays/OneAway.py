class Solution:
    def OneAway(self, s1: str, s2: str) -> bool:
        noOfOperations = 0
        len1 = len(s1)
        len2 = len(s2)
        if abs(len1 - len2) > 1:
            return False
        if len1 > len2:
            s1, s2 = s2, s1
            len1, len2 = len2, len1
        index1 = index2 = 0

        while index1 < len1 and index2 < len2:
            if s1[index1] != s2[index2]:
                noOfOperations += 1
                if noOfOperations > 1:
                    return False
                if len1 == len2:
                    index1 += 1

            else:
                index1 += 1
            index2 += 1
        return True

sol = Solution()
print(sol.OneAway("pale", "ple"))
print(sol.OneAway("pales", "pale"))
print(sol.OneAway("pale", "bale"))
print(sol.OneAway("pale", "bae"))
print(sol.OneAway("pale", "bae"))