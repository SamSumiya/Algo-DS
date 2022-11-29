const linkedListFindIter = ( head, target ) =>
{
    tail = head;

    while ( tail )
    {
        if ( tail.val === target )
        {
            return true;
        }
        tail = tail.next;
    }
    return false;
};


const linkedListFindRecur = ( head, target ) =>
{
    if ( head === null ) return false;
    if ( head.val === target ) return true;

    return linkedListFind( head.next, target );
};