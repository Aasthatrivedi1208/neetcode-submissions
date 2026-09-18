class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        res=[]
        s=set(nums)
        d = Counter(nums)
        if d[0]>1:
            return [0]*len(nums)


        for i in nums:
            if i != 0:
                p*=i
        for i in nums:
            if i == 0  :
                res.append(p)
            elif 0 in s:
                res.append(0)
            else:
                res.append(p//i)
        return res


        
        
        