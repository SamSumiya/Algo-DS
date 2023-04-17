var maxProfit = function (prices) {
  let i = 0
  let j = 1
  let diff = 0
  while (j < prices.length) {
    if (prices[i] > prices[j]) {
      i = j
    } else {
      if (prices[j] - prices[i] > diff) {
        diff = prices[j] - prices[i]
      }
      j += 1
    }
  }
  return diff
}
