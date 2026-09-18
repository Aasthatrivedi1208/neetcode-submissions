class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res=0
        for i in nums:
            count=1
            if i+1 not in s:
                while i-1 in s:
                    count += 1
                    i-=1
            res=max(res,count)
            print(res,count)

        return res
                    
        