class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}

        for ch in s:
            dict[ch] = dict.get(ch,0)+1


        for ch in t:
            if ch not in  dict:
                return False
            dict[ch] -= 1
            if dict[ch] < 0 :
                return False
        return True