def birthdayCakeCandles(candles):
    max_num = max(candles)
    counts = 0 
    
    for val in candles: 
        if val == max_num: 
                counts += 1
                
    return counts

def birthdayCakeCandles(candles):
        candles.sort()
        j = len(candles) - 1
        
        while j > 0:
                if candles[j] == candles[j-1]:
                        j -= 1 
                else: 
                        break 
        return len(candles) - j