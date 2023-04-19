class Node {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

const insertNode = (head, value, index) => {
  let tail = head
  if (index === 0) {
    const newNode = new Node(value)
    newNode.next = tail
    return newNode
  }

  while (tail) {
    index -= 1
    if (index === 0) {
      const newNode = new Node(value)
      newNode.next = tail.next
      tail.next = newNode
    }
    tail = tail.next
  }
  return head
}


const insertNode_recur = (head, value, index) => {
  if (index === 0) {
    const newNode = new Node(value)
    newNode.next = head
    return newNode
  } 
  
  if (index === 1) {
    const next = head.next
    head.next = new Node(value)
    head.next.next = next
    return head
  }
  
  insertNode(head.next, value, index - 1)
  return head 
};