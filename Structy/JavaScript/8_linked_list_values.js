const linkedListValues = (head) => {
  let op = []
  
  while(head) {
    op.push(head.val)
    head = head.next
  }
  return op
};


const linkedListValues_recur = (head) => {
  const values = [] 
  _likedListValues(head, values)
  return values
};

const _likedListValues = (head, values) => {
  if (head === null) return;
  values.push(head.val) 
  _likedListValues(head.next, values)
}