const zipperListsIter = ( head1, head2 ) =>
{
    let i = 0;
    let tail = head1;
    let tail1 = head1.next;
    let tail2 = head2;

    while ( tail1 && tail2 )
    {
        if ( i % 2 === 0 )
        {
            tail.next = tail2;
            tail2 = tail2.next;
        } else
        {
            tail.next = tail1;
            tail1 = tail1.next;
        }
        tail = tail.next;
        i += 1;
    }
    if ( tail1 ) tail.next = tail1;
    if ( tail2 ) tail.next = tail2;
    return head1;
};
