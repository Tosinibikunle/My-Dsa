class Solution(object):
    def numSteps(self, s):
        c=0
        while len(s)!=1:
            n=int(s,2)
            if s[-1]=='1':
                n+=1

            else:
                
                n=n//2
            s=bin(n)[2:]
            c+=1
        return c
