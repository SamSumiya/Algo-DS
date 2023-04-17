const compress = (s) => {
  s = s + '@'
  let op = ''
  let i = 0
  let j = 0

  while (j < s.length) {
    if (s[i] === s[j]) {
      j += 1
    } else {
      if (s.slice(i, j).length === 1) {
        op += s[i]
      } else {
        op += s.slice(i, j).length.toString() + s[i]
      }
      i = j
      j += 1
    }
  }
  return op
}

