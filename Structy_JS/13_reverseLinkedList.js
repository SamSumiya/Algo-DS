const reverseListIter = ( head ) =>
{
    tail = head;
    new_head = null;

    while ( tail )
    {
        next_node = tail.next;
        tail.next = new_head;
        new_head = tail;
        tail = next_node;
    }
    return new_head;
};


const reverseListRecur = ( head, new_head = null ) =>
{
    if ( head === null ) return new_head;

    next_node = head.next;
    head.next = new_head;

    return reverseList( next_node, head );
};