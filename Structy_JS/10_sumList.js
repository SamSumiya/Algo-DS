const sumListRecur1 = ( head ) =>
{
    let total = [];
    _sumList( head, total );
    return total.reduce( ( a, b ) => a + b, 0 );
};

const _sumList = ( head, total ) =>
{
    if ( head === null ) return 0;
    total.push( head.val );
    _sumList( head.next, total );
};








const sumListRecur2 = ( head ) =>
{
    if ( head === null ) return 0;
    return head.val + sumListRecur2( head.next );
};