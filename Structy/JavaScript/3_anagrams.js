const anagrams = (s1, s2) => {
  const hash = {}

  for (let el1 of s1) {
    if (!(el1 in hash)) {
      hash[el1] = 1
    } else {
      hash[el1] += 1
    }
  }

  for (el of s2) {
    if (s2.length < s1.length) return false
    if (el in hash) {
      hash[el] -= 1
      if (hash[el] < 0) {
        return false
      }
    } else {
      return false
    }
  }
  return true
}
