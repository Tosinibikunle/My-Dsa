class Solution:

    waves = []

    for i in range(1000):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10

        if (m > max(l, r)) or (m < min(l, r)):
            waves.append(i)

    def totalWaviness(self, A: int, B: int) -> int:
        return self.wave_count(B) - self.wave_count(A - 1)

    def wave_count(self, num: int) -> int:
        if num < 100:
            return 0

        res = 0

        for pattern in self.waves:
            res += self.count_ways(num, pattern)

        return res

    def count_ways(self, num: int, pattern: int) -> int:

        type_ = 1 if pattern < 100 else 0

        ways = 0
        mult = 1

        for _ in range(16):

            if mult * 100 > num:
                break

            pre = num // (mult * 1000)
            cur = (num // mult) % 1000
            suf = num % mult

            count = 0
            edge = 0

            if cur > pattern:

                count = pre - type_ + 1

            elif cur == pattern:

                count = max(0, pre - type_)

                if pre >= type_:
                    edge = suf + 1

            else:

                count = max(0, pre - type_)

            ways += count * mult + edge
            mult *= 10

        return ways
