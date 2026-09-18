class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set(nums)
        print(len(nums),len(s1))
        if len(nums)>len(s1):
            return True
        return False
        