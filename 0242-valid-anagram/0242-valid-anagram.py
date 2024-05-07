class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()

        if len(s) != len(t):
            return False
        else:
            if sorted(s) == sorted(t):
                return True
            return False