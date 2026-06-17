class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] ==')':
            return False
        top =-1
        star =0
        for i in range(len(s)):
            if s[i] == '(':
                top +=1
            elif s[i] == ')':
                if top<0:
                    if star:
                        star-=1
                    else:
                        return False
                else:
                    top-=1
            elif s[i] == '*':
                star+=1
        if star ==0 and top <=-1:
            return True
        elif top< star:
            return True
        return False
        

        