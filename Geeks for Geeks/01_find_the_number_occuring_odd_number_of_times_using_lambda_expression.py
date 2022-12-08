'''
Input :  [1, 2, 3, 2, 3, 1, 3]
Output :  3
'''


from functools import reduce

def oddTimes(input): 
    print(reduce(lambda a, b: a - b, input))
    return reduce(lambda a, b: a ^ b, input)

if __name__ == '__main__': 
    input = [1, 2, 3, 2, 3, 1, 3]
    oddTimes(input
    

    // const writeFilePromise = ( file, data ) =>
// {
//     return new Promise( ( resolve, reject ) =>
//     {
//         fs.writeFile( file, data, ( error ) =>
//         {
//             if ( error ) reject( 'Something went wrong...' );

//             resolve( 'success' );
//         } );
//     } );
// };