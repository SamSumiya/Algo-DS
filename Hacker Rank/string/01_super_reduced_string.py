def superReducedString(s):
    changed = True
    output = 'Empty String'

    while changed and s != "":
        changed = False
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                changed = True
                s = s[:(i)] + s[(i+2):]
                break

    return output if len(s) == 0 else s
