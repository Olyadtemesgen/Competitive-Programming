class Solution:
    def minimumSum(self, num: int) -> int:
        
        num = str(sorted(list(str(num))))
        
        list1 = [num[2]+num[17], num[7]+num[12]]

        return (int(list1[0])+int(list1[1]))
