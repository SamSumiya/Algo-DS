const pairSum = ( numbers, targetSum ) =>
{
    object = {};

    for ( let i = 0; i < numbers.length; i++ )
    {
        let diff = targetSum - numbers[ i ];
        if ( diff in object )
        {
            return [ i, object[ diff ] ];
        }
        object[ numbers[ i ] ] = i;
    }
    return;
};