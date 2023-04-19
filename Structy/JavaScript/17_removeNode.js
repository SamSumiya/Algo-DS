const removeNode = (head, targetVal) => {
  let tail = head
  let prev = null

  while (tail) {
    if (tail.val === targetVal && prev === null) {
      return tail.next
    }
    if (tail.val === targetVal) {
      prev.next = tail.next
      break
    }
    prev = tail
    tail = tail.next
  }
  return head
}
