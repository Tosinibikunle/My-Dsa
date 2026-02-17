from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hours in range(12):
            for minutes in range(60):
                if bin(hours).count('1') + bin(minutes).count('1') == turnedOn:
                    time = f"{hours}:{minutes:02d}" 
                    ans.append(time)
        return ans
