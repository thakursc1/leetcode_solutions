class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        a = max(candies)

        return [i+extraCandies>=a for i in candies]