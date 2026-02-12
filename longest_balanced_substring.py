class Solution:
    def longestBalanced(self, s: str) -> int:
        mp = {}
        sz = len(s)
        ans = 0
        
        for i in range(sz):
            mp.clear() # Emptying the dictionary
            for j in range(i, sz):
                char = s[j]
                mp[char] = mp.get(char, 0) + 1
                
                cnt = mp[char]
                flag = True
                
                # Check if all frequencies in the dictionary are equal
                for val in mp.values():
                    if val != cnt:
                        flag = False
                        break
                
                if flag:
                    ans = max(ans, j - i + 1)
        
        return ans
