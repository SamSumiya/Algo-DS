const intersection = ( a, b ) =>
{
    let output = [];
    b = new Set( b );
    for ( char of a )
    {
        if ( b.has( char ) )
        {
            output.push( char );
        }
    }
    return output;
};