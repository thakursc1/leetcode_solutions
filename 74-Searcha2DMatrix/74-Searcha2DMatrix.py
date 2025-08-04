# Last updated: 03/08/2025, 22:47:41
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows =  len(matrix)
        cols = len(matrix[0])
        left  =  0
        right = rows*cols


        while left < right:
            
            mid = left + (right - left)//2 
            
            r, c = mid // cols ,  mid % cols 
            print(mid, r, c)
            if matrix[r][c] == target:
                return True 

            elif matrix[r][c] < target:  
                left = mid + 1
            
            else: 
                right = mid 
        
        return False 





        
        