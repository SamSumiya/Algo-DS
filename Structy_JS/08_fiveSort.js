const fiveSort = ( nums ) =>
{
    let left = 0;
    let right = nums.length - 1;

    while ( left < right )
    {
        if ( nums[ right ] === 5 )
        {
            right -= 1;
        } else if ( nums[ left ] === 5 )
        {
            [ nums[ left ], nums[ right ] ] = [ nums[ right ], nums[ left ] ];
            left += 1;
        } else
        {
            left += 1;
        }
    }
    return nums;
};
