class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        k = ""
        t = ""
        for i in s:
            if i.isalnum() and i != " ":
                k += i
        for i in range(len(k)-1,-1,-1):
            t += k[i]
        print(k)
        print(t)
        if k == t:
            return True
        else:
            return False
