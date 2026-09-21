class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(0,len(nums)-2):
            k=len(nums)-1
            j=i+1
            while k>j:
                if nums[k]+nums[j]+nums[i] > 0:
                    k-=1
                elif nums[k]+nums[j]+nums[i] < 0:
                    j+=1
                else:
                    ans.add((nums[i], nums[j],nums[k]))
                    k-=1
                    j+=1
                    
        return list(ans)


                
        