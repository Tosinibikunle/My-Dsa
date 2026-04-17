class Solution:
    def findFinalValue(self, nums, original):
        def check(original):
            for num in nums:
                if num == original:
                    return True
            return False

        present = True
        while present:
            if check(original):
                original *= 2
            else:
                present = False

        return original
