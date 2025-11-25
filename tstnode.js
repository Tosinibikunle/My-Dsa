class TSTNode {

  constructor(char) {

    this.char = char;
    this.left = this.eq = this.right = null;
    this.isEnd = false;

  }
}

class TernarySearchTree {

  constructor() {

    this.root = null;
  }

  insert(word) {

    this.root = this._insert(this.root, word, 0);
  }

  _insert(node, word, idx) {

    let char = word[idx];
    if (!node) node = new TSTNode(char);

    if (char < node.char) {

      node.left = this._insert(node.left, word, idx);

    } else if (char > node.char) {
      
      node.right = this._insert(node.right, word, idx);

    } else {

      if (idx + 1 === word.length) node.isEnd = true;
      else node.eq = this._insert(node.eq, word, idx + 1);

    }

    return node;
  }

  search(word) {

    return this._search(this.root, word, 0);
  }

  _search(node, word, idx) {

    if (!node) return false;
    let char = word[idx];

    if (char < node.char) return this._search(node.left, word, idx);

    if (char > node.char) return this._search(node.right, word, idx);

    if (idx === word.length - 1) return node.isEnd;

    return this._search(node.eq, word, idx + 1);
    
  }
}
