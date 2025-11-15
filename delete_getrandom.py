import random
class RandomizedSet(object):

    def __init__(self):

        self.store = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.store:

            self.store.add(val)
            return True

        else:
            return False


        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """ 
        if val in self.store:

            self.store.remove(val)
            return True

        else:
            return False


        

    def getRandom(self):
        """
        :rtype: int
        """
        if len(self.store) >= 1:

            num = random.randint(0,len(self.store) - 1)
            mylist = list(self.store)
            return mylist[num]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()