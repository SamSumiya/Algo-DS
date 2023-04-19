class Node {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

const createLinkedList = (values) => {
  if (values.length === 0) return null
  let head = new Node('x')
  let tail = head

  for (el of values) {
    tail.next = new Node(el)
    tail = tail.next
  }
  return head.next
}


const createLinkedList_recur = (values) => {
  if (values.length === 0) return null
  
  let newNode = new Node(values[0])
  newNode.next = createLinkedList(values.slice(1)) 
  return newNode 
};
