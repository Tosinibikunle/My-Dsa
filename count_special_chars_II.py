class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
     
        low_map = {c: i for i, c in enumerate(word) if c.islower()}
        up_map = {c: i for i, c in reversed(list(enumerate(word))) if c.isupper()}
        
        last_lower = [low_map.get(chr(97 + i), -1) for i in range(26)]
        
     
        first_upper = [up_map.get(chr(65 + i), -1) for i in range(26)]
        
       
        return sum(
            low_idx != -1 and up_idx != -1 and low_idx < up_idx
            for low_idx, up_idx in zip(last_lower, first_upper)
        )
