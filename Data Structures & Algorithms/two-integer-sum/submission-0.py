class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if target == (nums[i] + nums[j]):
                    res.append(i)
                    res.append(j)
                j += 1
            i += 1
        return res