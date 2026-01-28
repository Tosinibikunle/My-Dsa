class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        ta=sum(apple)
        capacity.sort(reverse=True)        
        cu=0
        co=0
        for cap in capacity:
            cu+=cap
            co+=1
            if cu>=ta:
                return co
