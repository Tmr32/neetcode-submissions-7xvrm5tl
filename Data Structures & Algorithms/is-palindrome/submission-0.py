import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = filtered.lower()
        j = 0
        k = len(s) - 1

        while j < k:
            if s[k] != s[j]:
                return False
            
            j += 1
            k -= 1

        return True