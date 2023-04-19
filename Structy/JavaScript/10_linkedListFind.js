
const linkedListFind = (head, target) => {
  
  while (head) {
    if (head.val === target) return true
    head = head.next
  }
  return false 
};



const linkedListFind_recur = (head, target) => {
  if (head === null) return false
  if (target === head.val) return true
  return linkedListFind(head.next, target)
};