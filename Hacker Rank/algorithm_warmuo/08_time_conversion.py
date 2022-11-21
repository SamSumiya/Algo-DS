def timeConversion(s):

    last_two = s[-2:]
    time = s[:-2]
    print(time)
    h_m_s = time.split(':')
    print(h_m_s)
    hours = h_m_s[0]
    minutes = h_m_s[1]
    seconds = h_m_s[2]
    digit_hours = int(hours)
    if last_two == 'PM':
        if digit_hours < 12:
                digit_hours += 12
                hours = str(digit_hours)
                return ':'.join([hours, minutes, seconds])
        else: 
            return ':'.join([hours, minutes, seconds])
    else: 
        if digit_hours >= 12:
                digit_hours -= 12
                hours = str(digit_hours)
                return ':'.join(['0'+hours, minutes, seconds])
        else: 
            return ':'.join([hours, minutes, seconds])

time = '13:05:45AM'
r = timeConversion(time)
print(r)