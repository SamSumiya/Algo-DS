const mostFrequentChar = ( s ) =>
{
    alphabets = 'abcdefghijklmnopqrstuvwxyz';
    indices = [];
    orders = [];
    for ( let i = 0; i < 26; i++ )
    {
        orders.push( 0 );
    }

    for ( let char of s )
    {
        orders[ alphabets.indexOf( char ) ] += 1;
    }

    max_num = Math.max( ...orders );

    for ( let i = 0; i < orders.length; i++ )
    {
        if ( orders[ i ] == max_num )
        {
            indices.push( i );
        }
    }

    for ( let i = 0; i < s.length; i++ )
    {
        if ( orders[ alphabets.indexOf( s[ i ] ) ] == max_num )
        {
            return s[ i ];
        }
    }
};


const mostFrequentChar_2 = ( s ) =>
{
    count = {};

    for ( let char of s )
    {
        if ( !( char in count ) )
        {
            count[ char ] = 1;
        } else
        {
            count[ char ] += 1;
        }
    }

    output = null;
    for ( let char of s )
    {
        if ( output === null || count[ char ] > count[ output ] )
        {
            output = char;
        }
    }

    return output;
};


