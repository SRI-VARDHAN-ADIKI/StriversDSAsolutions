class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = ""
        for i in s:
            if ord(i) <= 122 and ord(i) >= 97:
                x += i
        if x == x[::-1]:
            return True
        else:
            return False
