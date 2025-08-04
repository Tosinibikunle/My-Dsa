class CentroidDecomposition {
    constructor(n) {
        this.n = n;
        this.adj = Array.from({ length: n }, () => []);
        this.subSize = Array(n).fill(0);
        this.centroidMarked = Array(n).fill(false);
        this.centroidTree = Array(n).fill(-1);
    }

    addEdge(u, v) {
        this.adj[u].push(v);
        this.adj[v].push(u);
    }

    dfsSize(u, p) {
        this.subSize[u] = 1;
        for (let v of this.adj[u]) {
            if (v !== p && !this.centroidMarked[v]) {
                this.dfsSize(v, u);
                this.subSize[u] += this.subSize[v];
            }
        }
    }

    findCentroid(u, p, totalSize) {
        for (let v of this.adj[u]) {
            if (v !== p && !this.centroidMarked[v] && this.subSize[v] > totalSize / 2) {
                return this.findCentroid(v, u, totalSize);
            }
        }
        return u;
    }

    decompose(u, parent = -1) {
        this.dfsSize(u, -1);
        const centroid = this.findCentroid(u, -1, this.subSize[u]);
        this.centroidMarked[centroid] = true;
        this.centroidTree[centroid] = parent;

        for (let v of this.adj[centroid]) {
            if (!this.centroidMarked[v]) {
                this.decompose(v, centroid);
            }
        }

        return centroid;
    }
}
