# Last updated: 03/08/2025, 09:11:10
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        left = 0 
        right = 10001

        INT_MAX = 2**31 - 1 

        while left < right:

            mid = left + (right - left)//2

            val = reader.get(mid)

            if val == target:
                return mid
            elif val == INT_MAX or val > target:
                right = mid 
            else:
                left = mid+1
        return -1 

            

        