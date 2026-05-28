class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Step 1: Track actual indices cleanly using single-pass maps
        low_map = {c: i for i, c in enumerate(word) if c.islower()}
        up_map = {c: i for i, c in reversed(list(enumerate(word))) if c.isupper()}
        
        # Expression 1: 26-element array for LAST lowercase positions (default to -1)
        last_lower = [low_map.get(chr(97 + i), -1) for i in range(26)]
        
        # Expression 2: 26-element array for FIRST uppercase positions (default to -1)
        first_upper = [up_map.get(chr(65 + i), -1) for i in range(26)]
        
        # Zip evaluation
        return sum(
            low_idx != -1 and up_idx != -1 and low_idx < up_idx
            for low_idx, up_idx in zip(last_lower, first_upper)
        )
