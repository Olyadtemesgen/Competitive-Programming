class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        ans = ["" for i in range(len(s))]
        for index in range(len(indices)):
            ans[indices[index]] = s[index]
        
        return "".join(ans)