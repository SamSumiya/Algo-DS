// class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

const longestStreak = (head) => {
  let count = 0
  let c = 1

  while (head) {
    next = head.next
    if (next !== null && head.val === next.val) {
      c += 1
    } else {
      if (c > count) {
        count = c
        c = 1
      }
    }
    head = head.next
  }

  return count
}


const longestStreak_1 = (head) => {
  let prevNodeVal = null
  let max = 0
  let current = 0
  
  while (head) {
    if (head.val === prevNodeVal) {
      current += 1
    } else {
      current = 1
    }
    
    if (current > max) max = current
    prevNodeVal = head.val
    head = head.next
  }
  return max 
};
