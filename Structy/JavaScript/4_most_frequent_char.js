const mostFrequentChar = (s) => {
  const dict = {}
  const store = []

  for (let el of s) {
    if (!(el in dict)) {
      dict[el] = 1
    } else {
      dict[el] += 1
    }
  }

  const maxNum = Math.max(...Object.values(dict))
  for (let el of s) {
    if (dict[el] === maxNum) {
      store.push(el)
    }
  }
  return store[0]
}
