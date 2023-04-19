const getNodeValue = (head, index) => {
  let i = 0

  while (head) {
    if (i === index) {
      return head.val
    }
    i += 1
    head = head.next
  }
  return null
}

const getNodeValue_reucur = (head, index) => {
  if (index < 0 || head === null) return null

  if (index === 0) return head.val

  return getNodeValue(head.next, index - 1)
}
