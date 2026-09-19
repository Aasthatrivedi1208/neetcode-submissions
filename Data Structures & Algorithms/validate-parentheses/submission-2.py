class Solution:
    def isValid(self, s: str) -> bool:
        op=0
        cl=0
        l=[]
        for br in s:
            if len(l)==0 and (br =='}' or br==']' or br == ')'):
                return False
            elif (br =='(' or br=='[' or br == '{'):
                l.append(br)
            else:
                if len(l)>0:
                    elem = l.pop()
                    if (elem == '(' and br == ')') or(elem == '[' and br == ']') or (elem == '{' and br == '}'):
                        continue
                    else:
                        return False

        if len(l)>0:
            return False
        else:
            return True

        