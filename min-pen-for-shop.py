class Solution:
    def bestClosingTime(self, customers):
        y_rem = customers.count('Y')
        nn = 0
        
        penalty = nn + y_rem
        min_p = penalty
        min_i = 0
        
        for i, char in enumerate(customers, start=1):
        
            if char == 'Y':
                y_rem -= 1
            else:
                nn += 1 
                
            penalty = nn + y_rem
            
            
            if penalty < min_p:
                min_p = penalty
                min_i = i
                
        return min_i
