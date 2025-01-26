class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = 0
        i = 1
        wrt = 0
        while i<len(chars):
            if chars[prev] != chars[i]:
                total = i - prev
                chars[wrt]=chars[prev]
                wrt+=1
                if total>1:
                    for k in str(i-prev):
                        chars[wrt]=k
                        wrt+=1
                prev = i
            i+=1
        
        total = i - prev
        chars[wrt]=chars[prev]
        wrt+=1
        if total>1:
            for i in str(i-prev):
                chars[wrt]=i
                wrt+=1
        return wrt