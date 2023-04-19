var pivotIndex = function (nums) {
  let leftSum = 0
  let totalSum = nums.reduce((a, c) => a + c)

  for (let i = 0; i < nums.length; i += 1) {
    totalSum -= nums[i]
    if (totalSum === leftSum) {
      return i
    }
    leftSum += nums[i]
  }

  return -1
}
