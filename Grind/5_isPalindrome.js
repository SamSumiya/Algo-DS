var isPalindrome = function (s) {
  const lowerS = s.toLowerCase()
  let formattedString = ''
  for (let el of lowerS) {
    if (el.match(/[a-z0-9]/)) {
      formattedString += el
    }
  }

  let star = 0
  let end = formattedString.length - 1

  while (star < end) {
    if (formattedString[star] !== formattedString[end]) {
      return false
    }
    star += 1
    end -= 1
  }
  return true
}
