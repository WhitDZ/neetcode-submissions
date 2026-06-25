class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1     
            else:
                s_dict[s[i]] = s_dict[s[i]] + 1 
            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 1     
            else:
                t_dict[t[i]] = t_dict[t[i]] + 1  
        return s_dict == t_dict
        