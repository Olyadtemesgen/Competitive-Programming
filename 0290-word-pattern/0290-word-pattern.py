class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return (False)
        dict = {}
        dict2 = {}
        for x in range(len(s)):
            if pattern[x] in dict and dict[pattern[x]] != s[x]:
                return False
            else:
                dict[pattern[x]] = s[x]
            if s[x] in dict2 and dict2[s[x]] != pattern[x]:
                return False
            else:
                dict2[s[x]] = pattern[x]
        return True