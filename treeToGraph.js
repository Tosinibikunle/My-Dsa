function treeToGraph(node, graph = {}, parent = null) {
  if (!node) return graph;
  if (!graph[node.val]) graph[node.val] = [];

  if (parent) {
    graph[node.val].push(parent.val);
    graph[parent.val].push(node.val);
  }

  for (let child of node.children || []) {
    treeToGraph(child, graph, node);
  }

  return graph;
}
