var createCounter = function(n) {
	n -= 1 
	return function() {
		n ++ 
		return n 
	};
};