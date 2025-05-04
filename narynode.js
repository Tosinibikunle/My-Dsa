class NaryNode {
 constructor(val) {
  this.val = val;
  this.children = [];
                }
                }

function traverseNary(node) {
  if (!node) return;
  console.log(node.val);
  for (let child of node.children) {
     traverseNary(child);
                            }
                            }
