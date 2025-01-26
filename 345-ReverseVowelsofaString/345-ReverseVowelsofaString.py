class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0 
        j = len(s)-1
        while i<j:
            while i<len(s) and s[i] not in "aAeEiIoOuU":
                i+=1
            while j>=0 and s[j] not in "aAeEiIoOuU":
                j-=1
            
            if j<=i:
                break
            if s[i] in "aAeEiIoOuU" and s[j] in "aAeEiIoOuU":
                s[i],s[j] = s[j], s[i]
            i+=1
            j-=1            
        
        return "".join(s)