class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 1
        l, r = 0, 1
        letters_seen = set(s[0])

        while r < len(s):
            if s[r] not in letters_seen:
                letters_seen.add(s[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                letters_seen.remove(s[l])
                l += 1

        return max_length