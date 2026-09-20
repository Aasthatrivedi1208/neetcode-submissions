class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans = []

        def dfs(ind,st):
            if len(st)==len(digits):
                ans.append(st)
                return
            
            for ch in d[digits[ind]]:
                dfs(ind+1,st+ch)

        if len(digits)==0:
            return []

        dfs(0,"")
        return ans
        