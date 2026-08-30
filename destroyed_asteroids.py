class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        MAXA = 100000
        cnt = [0] * (MAXA + 1)

        for ast in asteroids:
            cnt[ast] += 1

        curmass = mass

        for ast in range(1, MAXA + 1):
            while cnt[ast]:
                if curmass < ast:
                    return False

                curmass += ast
                cnt[ast] -= 1

        return True
