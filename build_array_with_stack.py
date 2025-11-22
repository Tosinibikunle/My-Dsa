# 🧩 LC 1441: Build an Array With Stack Operations

class Solution:
    def buildArray(self, target, n):
        ans = []
        stk = []
        ctn = 0
        index = 0
        
        for i in range(1, n + 1):
            if index >= len(target):
                break
            
            if target[index] == i:
                # pop extra elements before adding correct target element
                while stk and ctn:
                    stk.pop()
                    ans.append("Pop")
                    ctn -= 1
                stk.append(i)
                ans.append("Push")
                index += 1
            
            else:
                # push then pop since not in target
                stk.append(i)
                ans.append("Push")
                ctn += 1
        
        return ans