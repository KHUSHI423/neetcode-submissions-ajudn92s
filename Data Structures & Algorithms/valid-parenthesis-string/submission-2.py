class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ')':
            return False 
        top =-1
        star = 0
        i  = 0
        while i<len(s):
            if s[i] =='(':
                top+=1
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
            i+=1
        if top >=0 :
            if top <star:
                return True
            else:
                return False
        return True
    
                    
        