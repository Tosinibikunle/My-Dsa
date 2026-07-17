class Solution:
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)

    def gcdOfOddEvenSums(self, n: int) -> int:
        return self.gcd(n * n, n * (n + 1))
