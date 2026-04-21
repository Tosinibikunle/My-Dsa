def solve():
    # Read A, B, and N from input
    try:
        data = input().split()
        if not data:
            return
        
        a = int(data[0])
        b = int(data[1])
        n = int(data[2])
        
        # We already have the 1st (a) and 2nd (b) terms.
        # We need to calculate up to the Nth term.
        # We start the loop from 3 to N (inclusive).
        
        current_a = a
        current_b = b
        
        for _ in range(3, n + 1):
            # Calculate the next term: Tn+2 = (Tn+1)^2 + Tn
            next_term = (current_b ** 2) + current_a
            
            # Update the terms for the next iteration
            current_a = current_b
            current_b = next_term
            
        # If N was 1 or 2, the loop wouldn't run and 
        # we'd need logic for that, but constraints say N >= 3.
        print(current_b)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
