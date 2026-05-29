class Node:
    def __init__(self, best_idx: int = 0):
        self.best_idx = best_idx
        self.children = [None] * 26

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = Node()
        
        # Insert container words (reversed)
        for i, w in enumerate(wordsContainer):
            node = root
            # Update root best index: shortest word overall
            if len(wordsContainer[node.best_idx]) > len(w):
                node.best_idx = i
            
            for ch in reversed(w):
                idx = ord(ch) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = Node(i)
                else:
                    if len(wordsContainer[node.children[idx].best_idx]) > len(w):
                        node.children[idx].best_idx = i
                node = node.children[idx]
        
        # Answer queries
        ans = []
        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                idx = ord(ch) - ord('a')
                if not node.children[idx]:
                    break
                node = node.children[idx]
            ans.append(node.best_idx)
        return ans
