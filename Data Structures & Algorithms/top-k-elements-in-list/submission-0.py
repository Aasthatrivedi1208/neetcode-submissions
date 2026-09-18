class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        
        sorted_dict = dict(sorted(d.items(),key=lambda item:item[1],reverse=True))

        res= list(sorted_dict.keys())
        return res[0:k]


