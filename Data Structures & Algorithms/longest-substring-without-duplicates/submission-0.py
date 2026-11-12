class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        longestSub = 0
        left = 0
        right = 0
        for i in s:
            while i in found:
                found.remove(s[left])
                left += 1
            right += 1
            currLen = right-left
            if currLen > longestSub:
                longestSub = currLen
            found.add(i)

        return longestSub