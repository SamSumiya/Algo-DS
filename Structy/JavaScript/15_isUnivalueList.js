const isUnivalueList = (head) => {
  let value = null

  while (head) {
    if (value === null) {
      value = head.val
    } else if (value !== head.val) {
      return false
    }
    head = head.next
  }
  return true
}


const isUnivalueList_recur = (head) => {
  if (head.next === null) return true
  const next = head.next

  if (head.val !== next.val) return false
  return isUnivalueList(next)
};