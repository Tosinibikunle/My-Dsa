class Solution:
    def minimumEffort(self, shop: list[list[int]]) -> int:
        shop.sort(key=lambda x: x[1] - x[0], reverse=True)

        def test(bal):
            for cost, thresh in shop:
                if bal < thresh:
                    return False
                bal -= cost
            return True

        return bisect.bisect_left(range(10**9 + 1), True, key=test)
