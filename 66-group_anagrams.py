class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        arr = []
        for x in strs:
            arr.append(sorted(x))
        dict = {}
        for x in range(len(arr)):
            arr[x] = "".join(arr[x])
        for l in range(len(arr)):
            if arr[l] not in dict:
                dict[arr[l]] = [l]
            else:
                dict[arr[l]] += [l]
        other = []
        for dicts, others in dict.items():
            da = []
            for x in others:
                da.append(strs[x])
            other.append(da)
        return other
