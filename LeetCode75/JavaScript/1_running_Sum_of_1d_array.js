var runningSum = function (nums) {
  let i = 1

  for (i; i < nums.length; i++) {
    nums[i] = nums[i] + nums[i - 1]
  }

  return nums
}
