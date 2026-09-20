class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans =[]
        def dfs(ind,li):
            if sum(li)==target:
                ans.append(li.copy())
                return

            for i in range(ind,len(nums)):
                li.append(nums[i])
                if sum(li)<= target:
                    dfs(i,li)
                li.pop()
        
        dfs(0,[])
        return ans
