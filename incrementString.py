def increment_string(strng):
    if strng == '':
        return '1'
    else:
        aNumber = True
        numberToIncrement = ''
        indexTracker = -1
        while aNumber:
            if strng[indexTracker].isnumeric():
                numberToIncrement += str(strng[indexTracker])
                indexTracker -= 1
            else:
                aNumber = False
    numberToIncrement = numberToIncrement[::-1]
    if len(numberToIncrement) == 0:
        strng += '1'
        return strng
    else:
        zeroCount = 0
        zeroIndex = 0
        while numberToIncrement[zeroIndex] == '0' and zeroIndex < len(numberToIncrement) - 1:
            zeroCount += 1
            zeroIndex += 1
        intNumberToIncrement = int(numberToIncrement)
        originalLen = len(str(intNumberToIncrement))
        if len(str(intNumberToIncrement + 1)) == originalLen:
            finalText = (zeroCount * '0') + str(intNumberToIncrement + 1)
            strng = strng.replace(numberToIncrement, finalText)
            return strng
        else:
            finalText = (zeroCount - 1) * ('0') + str(intNumberToIncrement + 1)
            strng = strng.replace(numberToIncrement, finalText)
            return strng


print(increment_string('foobar001'))
print(increment_string('foobar1'))
print(increment_string('foo00'))
print(increment_string('foo0099'))
print(increment_string('foobar99'))
