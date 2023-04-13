var compose = function (functions) {
  return (fn = (x) => {
    if (functions.length === 0) return x
    for (let func of functions.reverse()) {
      x = func(x)
    }
    return x
  })
}
