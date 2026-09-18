class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d= defaultdict(list)
        res = []
        for i in strs:
            d[tuple(sorted(i))].append(i)
    
        return list(d.values())

        # for k,v in d.items():
        #     if len(v)==1:
        #         res.append(v)
        #     while len(v)>0:

                


        return res


        