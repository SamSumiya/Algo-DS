var timeLimit = function (fn, t) {
  return async function (...args) {
    const result = fn(...args)

    const rejected = new Promise((_, reject) => {
      setTimeout(() => reject('Time Limit Exceeded'), t)
    })

    return Promise.race([result, rejected])
  }
}
