class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # flowers to be potted until first non empty spot 

        i = 0
        spots = 0

        if len(flowerbed)==1 and flowerbed[i]==0:
            return n<=1

        while i<len(flowerbed) and flowerbed[i]==0:
            spots+=1
            i+=1
        if i==len(flowerbed):
            potted = (spots+1)//2
        else:
            potted = (spots)//2
        spots = 0
        while i<len(flowerbed):
            if flowerbed[i] == 1:
                if spots>=2:
                    potted+= (spots-2 + 1)//2
                spots = 0
            else:
                spots+=1

            if potted >=n:
                return True 
            i+=1
            
        # Finally remaining spots
        potted += (spots)//2
        return potted>=n 