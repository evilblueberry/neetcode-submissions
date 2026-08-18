class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)


        top_k = heapq.nlargest(k, counts.keys(), key=counts.get)
        return top_k