var map = function (arr, fn) {
  const op = []

  for (let i = 0; i < arr.length; i++) {
    op.push(fn(arr[i], i))
  }

  return op
}
