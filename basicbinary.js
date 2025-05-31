// Define a Node in the binary tree
class TreeNode {
  constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
      }
    }

                // Define the Binary Tree structure
class BinaryTree {
   constructor() {
      this.root = null;
       }

                          // Insert value into the binary tree (non-BST)
   insert(value) {
       const newNode = new TreeNode(value);

       if (!this.root) {
         this.root = newNode;
         return;
     }

   const queue = [this.root];

   while (queue.length) {
      const current = queue.shift();

      if (!current.left) {
           current.left = newNode;
           break;
  } else {
       queue.push(current.left);
   }

                                                                                                                  if (!current.right) {
                                                                                                                          current.right = newNode;
                                                                                                                                  break;
                                                                                                                                        } else {
                                                                                                                                                queue.push(current.right);
                                                                                                                                                      }
                                                                                                                                                          }
                                                                                                                                                            }

                                                                                                                                                              // Simple in-order traversal
                                                                                                                                                                inorder(node = this.root) {
                                                                                                                                                                    if (node) {
                                                                                                                                                                          this.inorder(node.left);
                                                                                                                                                                                console.log(node.value);
                                                                                                                                                                                      this.inorder(node.right);
                                                                                                                                                                                          }
                                                                                                                                                                                            }
                                                                                                                                                                                            }

                                                                                                                                                                                            // Example Usage
                                                                                                                                                                                            const tree = new BinaryTree();
                                                                                                                                                                                            tree.insert(10);
                                                                                                                                                                                            tree.insert(20);
                                                                                                                                                                                            tree.insert(30);
                                                                                                                                                                                            tree.insert(40);

                                                                                                                                                                                            console.log("In-order traversal:");
                                                                                                                                                                                            tree.inorder();