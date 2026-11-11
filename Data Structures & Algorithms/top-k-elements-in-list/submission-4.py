class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_elements = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        result = sorted_elements[:k]

        return result