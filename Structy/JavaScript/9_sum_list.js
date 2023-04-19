const sumList = (head) => {
  let sum = 0
  while (head) {
    sum += head.val
    head = head.next
  }
  return sum
};


const sumList_recur = (head) => {
  if (head === null) return 0
  return head.val + sumList(head.next)
};