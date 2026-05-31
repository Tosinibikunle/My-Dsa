class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        MAXA = 100000
        cnt = [0] * (MAXA + 1)

        # Count frequency of each asteroid size
        for ast in asteroids:
            cnt[ast] += 1

        curmass = mass

        # Process asteroids from smallest to largest
        for ast in range(1, MAXA + 1):
            while cnt[ast]:
                if curmass < ast:
                    return False

                curmass += ast
                cnt[ast] -= 1

        return True
