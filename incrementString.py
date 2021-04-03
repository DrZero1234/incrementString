#!python3
# incrementString.py


def increment_string(strng):
    # In case of blank string the return Value will be "1"
    if strng == '':
        return '1'
    # Checks the string from the last character to the first and while the character is numeric the character will be added to a variavle
    else:
        # The last numeric string is stored in numberToIncrement
        numberToIncrement = ''
        indexTracker = -1
        try:
            while strng[indexTracker].isnumeric():
                numberToIncrement += str(strng[indexTracker])
                indexTracker -= 1
        except IndexError:
            pass
    # Reversing the variable since it stores it from back
    numberToIncrement = numberToIncrement[::-1]
    # If the last character in the original string is not a number we just add the '1' to the string
    if len(numberToIncrement) == 0:
        strng += '1'
        return strng
    else:
        # Setup varibles for the index and the consecutive '0' counter
        zeroCount = 0
        zeroIndex = 0
        # We iterate over the number we got from the original string and while the value of the iteration is '0' we add +1 to the '0' counter
        while numberToIncrement[zeroIndex] == '0' and zeroIndex < len(numberToIncrement) - 1:
            zeroCount += 1
            zeroIndex += 1
        # Variables for the integer version of the string and to store the length of the integer value since it doesnt store the '0'-s
        intNumberToIncrement = int(numberToIncrement)
        originalLen = len(str(intNumberToIncrement))
        # We check if adding 1 to the integer will change the length of the number
        # for example adding 1 to 9 the integer value originally the length was 1 but now its 2 becasue the len of ('10') is 2
        if len(str(intNumberToIncrement + 1)) == originalLen:
            # If the len stayed intact we just add the amount of '0'-s we counted and the integer Value + 1
            finalText = (zeroCount * '0') + str(intNumberToIncrement + 1)
            strng = strng.replace(numberToIncrement, finalText)
            return strng
            # However if the len of the number changed we decrease the zero Counter by 1 and the adding the 0-s and integer values to the string
        else:
            finalText = (zeroCount - 1) * ('0') + str(intNumberToIncrement + 1)
            strng = strng.replace(numberToIncrement, finalText)
            return strng


print(increment_string('foobar001'))
print(increment_string('foobar1'))
print(increment_string('foo00'))
print(increment_string('foo0099'))
print(increment_string('foobar99'))
print(increment_string('1'))
