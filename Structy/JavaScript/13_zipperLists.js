// class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

const zipperLists = (head1, head2) => {
  let count = 0
  let next1 = head1.next
  let tail = head1

  while (next1 && head2) {
    if (count % 2 === 0) {
      tail.next = head2
      head2 = head2.next
    } else {
      tail.next = next1
      next1 = next1.next
    }
    count += 1
    tail = tail.next
  }

  if (next1) {
    tail.next = next1
  }
  if (head2) {
    tail.next = head2
  }

  return head1
}


const zipperLists_recur = (head1, head2) => {
  if (head1 === null && head2 === null) return null
  if (head1 === null) return head2
  if (head2 === null) return head1
  const next1 = head1.next
  const next2 = head2.next

  head1.next = head2
  head2.next = zipperLists(next1, next2)
  return head1
}

