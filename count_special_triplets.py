class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        z1,z2 = Counter(),Counter()
        return sum((z2[v/2],z2.update({v:z1[v*2]}),z1.update([v]))[0]
            for v in a)%(10**9+7)
