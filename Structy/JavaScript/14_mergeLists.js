
const mergeLists_recur = (head1, head2) => {
  if ( head1 === null && head2 === null ) return
  if ( head1 === null ) return head2
  if ( head2 === null ) return head1 
  
  if (head1.val < head2.val) {
    const next1 = head1.next 
    head1.next = mergeLists(next1, head2)
    return head1 
  } else {
    const next2 = head2.next 
    head2.next = mergeLists(head1, next2)
    return head2
  }
};