var mergeTwoLists = function (l1, l2) {
  let tempNode = new ListNode(0, null)
  let currentNode = tempNode
  while (l1 && l2) {
    if (l1.val <= l2.val) {
      currentNode.next = l1
      l1 = l1.next
    } else {
      currentNode.next = l2
      l2 = l2.next
    }
    currentNode = currentNode.next
  }
  currentNode.next = l1 || l2
  return tempNode.next
}
