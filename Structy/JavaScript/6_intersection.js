const intersection = (a, b) => {
  let op = [] 
  let setB = new Set(b)
  
  for (let el of a) {
    if (setB.has(el)) {
      op.push(el)
    }
  }
  return op
};