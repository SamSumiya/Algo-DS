const uncompress = ( s ) =>
{
    let i = ( j = 0 );
    const len = s.length;
    numbers = "1234567890";
    let output = "";

    while ( j < len )
    {
        if ( numbers.includes( s[ j ] ) )
        {
            j++;
        } else
        {
            range = s.slice( i, j );
            for ( let count = 0; count < range; count++ )
            {
                output += s[ j ];
            }
            j += 1;
            i = j;
        }
    }
    return output;
};
