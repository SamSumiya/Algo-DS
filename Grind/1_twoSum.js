var twoSum = function (nums, target) {
  const op = {}

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    const diff = target - num

    if (diff in op) {
      console.log(diff, op, i, op[diff.toString()])
      return [op[diff.toString()], i]
    } else {
      op[num] = i
    }
  }
}
