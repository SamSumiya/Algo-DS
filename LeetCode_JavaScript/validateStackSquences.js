var validateStackSequences = function(pushed, popped) {
	let i = 0
	let stack = [] 

	for (let p of pushed) {
			stack.push(p)
			while (i < popped.length && stack[stack.length - 1] === popped[i]) {
					stack.pop()
					i += 1
			}
	}
	return i === popped.length
};