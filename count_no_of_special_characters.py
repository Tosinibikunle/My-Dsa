class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low = [False] * 26
        up = [False] * 26

        for c in word:
            # Lowercase character
            if 'a' <= c <= 'z':
                low[ord(c) - ord('a')] = True

            # Uppercase character
            else:
                up[ord(c) - ord('A')] = True

        ans = 0

        # Count characters present in both
        for i in range(26):
            if low[i] and up[i]:
                ans += 1

        return ans
