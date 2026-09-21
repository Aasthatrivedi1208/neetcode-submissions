class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =[1]*len(nums)
        for i in range(1,len(nums)):
            j=0
            while j<i:
                ans=1
                if nums[i]>nums[j]:
                    ans+=dp[j]
                dp[i]=max(dp[i],ans)
                j+=1
        return max(dp)


