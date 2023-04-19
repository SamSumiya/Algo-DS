const reverseList = (head) => {
  let current = head
  let prev = null

  while (current !== null) {
    const next = current.next
    current.next = prev
    prev = current
    current = next
  }
  return prev
};

const reverseList_recur = (head) => {
  if (head === null) return prev
  const next = head.next
  head.next = prev 
  return reverseList(next, head);
};