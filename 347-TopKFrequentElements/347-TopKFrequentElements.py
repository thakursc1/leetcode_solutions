# Last updated: 01/08/2025, 09:17:34
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_freq = Counter(nums)

        top_k = []

        for i, freq in nums_freq.items():
            if len(top_k) < k:
                heapq.heappush(top_k, (freq, i))
            
            elif freq > top_k[0][0]:
                heapq.heapreplace(top_k, (freq, i))

        return [i[1] for i in top_k]