class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0

        for pattern in patterns:
            if word.find(pattern) != -1:
                ans += 1

        return ans
