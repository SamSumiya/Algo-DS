var filter = function (arr, fn) {
  const res = [];
  let i = 0;
  for (let a of arr) {
    if (fn(a, i)) res.push(a);
    i += 1;
  }
  return res;
};
