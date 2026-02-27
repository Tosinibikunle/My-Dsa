class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from collections import defaultdict

        # Preprocess allowed patterns
        mp = defaultdict(list)
        for s in allowed:
            mp[s[:2]].append(s[2])

        self.bad = set()
        return self.check(bottom, mp)

    def check(self, curr: str, mp) -> bool:
        # Base case: reached the top
        if len(curr) == 1:
            return True

        # Memoized failed state
        if curr in self.bad:
            return False

        next_rows = []
        self.formation(0, curr, mp, [], next_rows)

        for row in next_rows:
            if self.check(row, mp):
                return True

        # Mark this row as impossible
        self.bad.add(curr)
        return False

    def formation(self, i: int, bottom: str, mp, curr: list, res: list):
        if i == len(bottom) - 1:
            res.append("".join(curr))
            return

        key = bottom[i:i+2]
        if key not in mp:
            return

        for ch in mp[key]:
            curr.append(ch)
            self.formation(i + 1, bottom, mp, curr, res)
            curr.pop()  # backtrack
