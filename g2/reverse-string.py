class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        half = len(s) // 2
        for idx in range(len(s)):
            if not half:
                break
            half -= 1
            s[idx], s[len(s) - 1 - idx] = s[len(s) - 1 - idx] , s[idx]        