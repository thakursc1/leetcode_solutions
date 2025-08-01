# Last updated: 01/08/2025, 12:13:10
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in range(9):
            cache = set()
            for col in range(9):
                if board[row][col]!=".":
                    if board[row][col] not in cache:
                        cache.add(board[row][col])
                    else:
                        print(row, col)
                        return False 
        
        for col in range(9):
            cache = set()
            for row in range(9):
                if board[row][col]!=".":
                    if board[row][col] not in cache:
                        cache.add(board[row][col])
                    else:
                        return False 
        
        rng = {
            0:[0,1,2],
            1:[3,4,5],
            2:[6,7,8]
        }

        for i in range(3):
            for j in range(3):
                cache = set()
                for row in rng[i]:
                    for col in rng[j]:
                        if board[row][col]!=".":
                            if board[row][col] not in cache:
                                cache.add(board[row][col])
                            else:
                                return False 
                    
        return True 



                

