class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        
        if tot%2!=0:
            return False
        
        tot //= 2
        st = {0}
        
        index = len(nums) - 1
        
        for x in range(index, -1, -1):
            
            if tot in st:
                return True
            
            new = {0}
            for xx in st:
                new.add(xx + nums[x])
            
            st = st.union(new)
            # st.add(nums[x])
            
            st.add(nums[x])
            
            if tot in st:
                return True
        
        return False