def digit_square_sum(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(n):
        visited = set()

        while n not in visited:
            if n == 1:
                return True

            visited.add(n)
            n = self.digit_square_sum(n)

        return False