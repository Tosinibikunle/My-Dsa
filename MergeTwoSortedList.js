var mergeTwoLists = function(l1, l2) {
    if (!l1) {
      return l2;
    }
    if (!l2) {
      return l1;
    }
    const val1 = l1.val;
    const val2 = l2.val;
    let mergedNode;
    if (val1 < val2) {
      mergedNode = new ListNode(val1);
      mergedNode.next = mergeTwoLists(l1.next, l2);
    } else {
      mergedNode = new ListNode(val2);
      mergedNode.next = mergeTwoLists(l2.next, l1);
    }
    return mergedNode;
  };