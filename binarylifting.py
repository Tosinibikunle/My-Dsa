import math
from collections import deque

class BinaryLifting:
    def __init__(self, n, adj, root=0):
        
        self.n = n
        self.adj = adj
        self.root = root
        self.LOG = math.ceil(math.log2(n)) + 1
        self.timer = 0
        
        # up[u][i] stores the 2^i-th ancestor of u
        self.up = [[-1] * self.LOG for _ in range(n)]
        
        # Discovery times for O(1) ancestry check (optional optimization)
        self.tin = [0] * n
        self.tout = [0] * n
        
        # Depth for level alignment
        self.depth = [0] * n
        
        self._build()

    def _build(self):
        """
        BFS/DFS to compute depths and 2^0 parent, 
        then DP to compute 2^i parents.
        """
        # BFS is safer against recursion limits for deep trees
        queue = deque([self.root])
        visited = [False] * self.n
        visited[self.root] = True
        
        # 2^0 parent of root is itself (or -1, depending on preference)
        self.up[self.root][0] = self.root 
        
        order = [] # Process order for DP

        while queue:
            u = queue.popleft()
            order.append(u)
            
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    self.depth[v] = self.depth[u] + 1
                    self.up[v][0] = u
                    queue.append(v)
        
        # Compute binary lifting table: up[u][i] = up[ up[u][i-1] ][ i-1 ]
        # We process in BFS order ensures parents are ready
        for u in order:
            for i in range(1, self.LOG):
                parent_halfway = self.up[u][i-1]
                if parent_halfway != -1:
                    self.up[u][i] = self.up[parent_halfway][i-1]
                else:
                    self.up[u][i] = -1

    def get_kth_ancestor(self, node, k):
        """
        Finds the k-th ancestor of a node using binary lifting.
        Complexity: O(log k)
        """
        for i in range(self.LOG):
            if (k >> i) & 1:
                node = self.up[node][i]
                if node == -1: return -1
        return node

    def get_lca(self, u, v):
        """
        Finds the Lowest Common Ancestor of u and v.
        Complexity: O(log N)
        """
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # 1. Lift u to the same depth as v
        u = self.get_kth_ancestor(u, self.depth[u] - self.depth[v])
        
        if u == v:
            return u
        
        # 2. Lift both until they are just below the LCA
        for i in range(self.LOG - 1, -1, -1):
            if self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]
                
        # The parent of the current node is the LCA
        return self.up[u][0]

# --- Example Usage ---
if __name__ == "__main__":
    # Example Tree:
    #       0
    #      / \
    #     1   2
    #    / \
    #   3   4
    #      / \
    #     5   6
    
    n = 7
    adj = [[] for _ in range(n)]
    edges = [(0,1), (0,2), (1,3), (1,4), (4,5), (4,6)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    bl = BinaryLifting(n, adj, root=0)
    
    print(f"LCA of 5 and 6: {bl.get_lca(5, 6)} (Expected: 4)")
    print(f"LCA of 3 and 6: {bl.get_lca(3, 6)} (Expected: 1)")
    print(f"2nd Ancestor of 5: {bl.get_kth_ancestor(5, 2)} (Expected: 1)")
