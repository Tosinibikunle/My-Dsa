class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 19 -> 1**2 + 9**2 -> 82 -> 64 + 4 -> 68 -> 36 + 64 -> 100 -> 1

        store = []
        string_n = str(n)

        while n != 1:
            temp = 0

            for num in string_n:
                temp += int(num)*int(num) 

            n = temp
            
            if temp in store:
                print(store)
                return False
            else:
                store.append(temp)

        
        return True