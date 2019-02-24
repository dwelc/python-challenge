# Function to validate a string:
#
# The string is considered valid if every character
# in the string appears the same number of times.
# The string is also valid we can make one single character subtraction
# and have all characters remaining appear the same number of times


def IsValid(s):
    # Check input is present
    if not s:
        print('Entry is empty......exiting')
        return 'NO'

    # Remove any whitespace
    s = s.replace(" ", "")

    # Create a list of character counts
    cc = [s.count(letter) for letter in set(s)]

    # If only 1 character instance present, return NO
    if len(cc) == 1:
        return 'NO'

    # If all entrys are the same, return YES
    if max(cc)-min(cc) == 0:
        return 'YES'

    # If a single character exists, remove up to 1
    # from the list, if all entries are the same return YES
    # If not return NO
    if 1 in cc:
        cc.remove(1)
        if max(cc)-min(cc) == 0:
            return 'YES'
        else:
            return 'NO'

    # If gap between highest/lowest is 1 and only one character
    # has highest count, then we can subtract 1 and have parity, return YES
    if cc.count(max(cc)) == 1 and max(cc) - min(cc) == 1:
        return 'YES'

    # If None of the above conditions are met return NO
    else:
        return 'NO'


s = input('Enter the string:')
result = IsValid(s)
print(result)
