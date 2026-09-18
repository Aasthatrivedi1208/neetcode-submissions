class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[i for i in s]
        s1.sort()
        t1=[i for i in t]
        t1.sort()

        if len(s1) != len(t1):
            return False
        else:
            for i in range(len(s1)):
                if s1[i]!=t1[i]:
                    return False
                else:
                    continue
            return True

        