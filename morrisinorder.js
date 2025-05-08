function morrisInorder(root) {
      let curr = root;
        while (curr) {
            if (!curr.left) {
                  console.log(curr.val);
                        curr = curr.right;
                            } else {
                                  let pred = curr.left;
                                        while (pred.right && pred.right !== curr) {
                                                pred = pred.right;
                                                      }

                                                            if (!pred.right) {
                                                                    pred.right = curr;  // Threading
                                                                            curr = curr.left;
                                                                                  } else {
                                                                                          pred.right = null;  // Remove thread
                                                                                                  console.log(curr.val);
                                                                                                          curr = curr.right;
                                                                                                                }
                                                                                                                    }
                                                                                                                      }
                                                                                                                      }
