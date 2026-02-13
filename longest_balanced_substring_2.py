class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        a = b = c = ans = 0
        mp = {0: -1}
        M = 2 * n + 7
        
        for i, ch in enumerate(s):
            a += ch == 'a'
            b += ch == 'b'
            c += ch == 'c'
            k = (a - b) * M + (a - c)
            if k in mp:
                ans = max(ans, i - mp[k])
            else:
                mp[k] = i
        
        def f(x, y):
            nonlocal ans
            p = 0
            mp2 = {0: -1}
            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    p = 0
                    mp2 = {0: i}
                    continue
                p += 1 if ch == x else -1
                if p in mp2:
                    ans = max(ans, i - mp2[p])
                else:
                    mp2[p] = i
        
        for x, y in [('a', 'b'), ('a', 'c'), ('b', 'c')]:
            f(x, y)
        
        for ch in 'abc':
            cst = 0
            for ch2 in s:
                cst = cst + 1 if ch2 == ch else 0
                ans = max(ans, cst)
        
        return ans
