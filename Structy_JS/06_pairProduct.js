const pairProduct = (numbers, targetProduct) => {
    const object = {} 
    
    for (let i = 0; i < numbers.length; i++) {
      const diff = targetProduct / numbers[i]
      if (diff in object) {
        return [object[diff], i]
      }
      object[numbers[i]] = i
    }
    return 
  };