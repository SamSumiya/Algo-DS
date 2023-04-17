var isValid = function (s) {
  if (s.length % 2 !== 0) return false

  const brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
  }

  let bracketsQueue = []

  for (let i = 0; i < s.length; i++) {
    let el = s[i]
    if (brackets[el]) {
      bracketsQueue.push(brackets[el])
    } else if (el !== bracketsQueue.pop()) {
      return false
    }
  }
  return !bracketsQueue.length
}
