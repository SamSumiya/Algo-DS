const linkedListValuesIter = ( head ) =>
{
    const output = [];

    while ( head )
    {
        output.push( head.val );
        head = head.next;
    }
    return output;
};


const linkedListValuesRecur = ( head ) =>
{
    const values = [];
    _linledListValues( head, values );
    return values;
};

const _linledListValues = ( head, values ) =>
{
    if ( head === null ) return;
    values.push( head.val );
    _linledListValues( head.next, values );
};
