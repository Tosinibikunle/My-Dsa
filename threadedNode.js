class ThreadedNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
        this.isThreaded = false; // if right is a thread to inorder successor
    }
}
