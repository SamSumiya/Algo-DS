const pairSum = (numbers, targetSum) => {
  const dict = {}
  let i = 0
  for (let num of numbers) {
    const diff = targetSum - num
    if (diff in dict) {
      return [i, dict[diff]]
    } else {
      dict[num] = i
    }
    i += 1
  }
}
