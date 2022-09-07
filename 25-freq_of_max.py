class Solution:
  #This is the program I coded and it turned out that the time exceeded from the requirement,please help me out to get the problem.
    def maxFrequency(self, nums, k) :
        Rpointer, Lpointer, new_l = 1, 0, 0
        nums.sort()
        Windowslider=[]
        while Rpointer >= Lpointer and (len(nums[Lpointer:]) >= new_l:
            Windowslider = nums[Lpointer:Rpointer]
            if len(Windowslider) * nums[Rpointer - 1] <= sum(Windowslider) + k and Rpointer < len(nums):
                new_l = max(new_l, len(Windowslider))
                Rpointer += 1
            elif len(Windowslider) * nums[Rpointer - 1] <= sum(Windowslider) + k and Rpointer == len(nums):
                    new_l = max(new_l, len(Windowslider))
                    Lpointer += 1
            else:
                Lpointer += 1
        return new_l
    #this is the program I got from google
    def maxFrequency2(self, nums, k):
        ans = 0
        sum = 0

        nums.sort()

        l = 0
        for r, num in enumerate(nums):
            sum += num
            while sum + k < num * (r - l + 1):
                sum -= nums[l]
                l += 1
        ans = max(ans, r - l + 1)
        return ans
