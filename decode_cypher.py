from collections import defaultdict

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        if n == 0:
            return ""

        cols = n // rows
        mpp = defaultdict(list)

        for row in range(rows):
            for col in range(cols):

                # Only take valid diagonal cells
                if col >= row:
                    key = col - row
                    mpp[key].append(encodedText[row * cols + col])

        # Build result
        ans = []
        for key in sorted(mpp.keys()):
            ans.extend(mpp[key])

        result = "".join(ans)

        # Remove trailing spaces
        return result.rstrip()
