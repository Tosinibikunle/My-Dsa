from collections import defaultdict

class Solution:
    def decodeCiphertext(self, encodedText, rows):
        n = len(encodedText)
        if n == 0:
            return ""

        cols = n // rows
        mpp = defaultdict(list)

        for row in range(rows):
            for col in range(cols):

        
                if col >= row:
                    key = col - row
                    mpp[key].append(encodedText[row * cols + col])

        
        ans = []
        for key in sorted(mpp.keys()):
            ans.extend(mpp[key])

        result = "".join(ans)

    
        return result.rstrip()
