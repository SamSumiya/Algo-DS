const compress = ( s ) =>
{
    output = '';
    s = s + '!';
    let i = 0;
    let j = 0;
    count = 0;

    while ( j < s.length )
    {
        if ( s[ i ] === s[ j ] )
        {
            count += 1;
            j += 1;
        } else
        {
            if ( count === 1 )
            {
                output += s[ i ];
            } else
            {
                output += String( count ) + s[ i ];
            }

            count = 0;
            i = j;
        }
    }
    return output;
};

module.exports = {
    compress,
};
