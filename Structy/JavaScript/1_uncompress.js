const uncompress = (s) => {
  let i = 0
  let j = 0
  let op = ''
  const numbers = '0123456789'
	
  while (j < s.length) {
    if (numbers.includes(s[j])) {
      j += 1
    } else {
      const repeat = +s.slice(i, j)
      for (let k = 0; k < repeat; k++) {
        op += s[j]
      }
      j += 1
      i = j
    }
  }
  return op
}
