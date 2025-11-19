class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}

        for num in nums:

            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        

        max_value = float("-inf")
        final = None

        for key, value in store.items():

            if max_value < value:
                final = key
                max_value = value

        return final