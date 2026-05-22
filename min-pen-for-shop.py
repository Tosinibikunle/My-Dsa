class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_rem = customers.count('Y')
        nn = 0
        
        penalty = nn + y_rem
        min_p = penalty
        min_i = 0
        
        for i, char in enumerate(customers, start=1):
            # Evaluate current hour's customer
            if char == 'Y':
                y_rem -= 1
            else:
                nn += 1 
                
            penalty = nn + y_rem
            
            # Update minimum penalty and index
            if penalty < min_p:
                min_p = penalty
                min_i = i
                
        return min_i
