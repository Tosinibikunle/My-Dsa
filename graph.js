class Graph {
      constructor() {
          this.adjList = new Map();
    }

   addVertex(vertex) {
       if (!this.adjList.has(vertex)) {
           this.adjList.set(vertex, []);
           }
            }

   addEdge(vertex1, vertex2) {
        this.addVertex(vertex1);
        this.addVertex(vertex2);
        this.adjList.get(vertex1).push(vertex2);
        this.adjList.get(vertex2).push(vertex1); // Remove this for a directed graph
        }

   printGraph() {
      for (let [vertex, edges] of this.adjList.entries()) {
          console.log(`${vertex} -> ${edges.join(', ')}`);
            }   
         }
    
  bfs(start) {
      const visited = new Set();
      const queue = [start];                                                                           
      while (queue.length) {
      const vertex = queue.shift();
      if (!visited.has(vertex)) {
          console.log(vertex);
           visited.add(vertex);
           const neighbors = this.adjList.get(vertex);
           for (let neighbor of neighbors) {
              if (!visited.has(neighbor)) {
                 queue.push(neighbor);
                        }
                  }
               }
        }     
     }

                                                                                                                                                                                        dfs(start, visited = new Set()) {
                                                                                                                                                                                            if (visited.has(start)) return;
                                                                                                                                                                                                console.log(start);
                                                                                                                                                                                                    visited.add(start);

                                                                                                                                                                                                        for (let neighbor of this.adjList.get(start)) {
                                                                                                                                                                                                              this.dfs(neighbor, visited);
                                                                                                                                                                                                                  }
                                                                                                                                                                                                                    }
                                                                                                                                                                                                                    }
