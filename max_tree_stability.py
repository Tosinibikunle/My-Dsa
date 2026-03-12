class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def maxStability(self, n, edges, k):

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            good = []
            upgrade = []

            # mandatory edges
            for u,v,s,m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used += 1

            # classify optional edges
            for u,v,s,m in edges:
                if m == 0:
                    if s >= x:
                        good.append((u,v))
                    elif s*2 >= x:
                        upgrade.append((u,v))

            # use good edges first
            for u,v in good:
                if used == n-1:
                    break
                if dsu.union(u,v):
                    used += 1

            # then upgraded edges
            for u,v in upgrade:
                if used == n-1:
                    break
                if upgrades == k:
                    break
                if dsu.union(u,v):
                    upgrades += 1
                    used += 1

            return used == n-1


        left = 0
        right = max(s for _,_,s,_ in edges) * 2
        ans = -1

        while left <= right:
            mid = (left + right)//2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
