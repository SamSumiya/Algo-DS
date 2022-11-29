const getNodeValueIter = ( head, index ) =>
{
    while ( index > 0 )
    {
        if ( !head.next ) return null;
        head = head.next;
        index -= 1;
    }
    return head.val;
};


const getNodeValueRecur = ( head, index ) =>
{
    if ( index === 0 ) return head.val;
    if ( head === null ) return null;
    return getNodeValue( head.next, index - 1 );
};