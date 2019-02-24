# Script to validate a string:
#
# The string is considered valid if every character
# in the string appears the same number of times.
# The string is also valid we can make one single character subtraction
# and still have all characters appearing the same number of times

# Capture String input
s = input('Enter the string:')

# Check input is present
if not s:
    print('Entry is empty......exiting')
    quit()

# Create a list of character counts
cc = [s.count(letter) for letter in set(s)]
print('List Is:', cc)

# If only 1 character present, print NO
if len(cc) == 1:
    print('NO')
    quit()

# If all entrys are the same, print YES
if max(cc)-min(cc) == 0:
    print('YES')
    quit()

# If A single character exists, remove up to 1
# from the list and check if all entries are the same
if 1 in cc:
    print('Found Single Character')
    cc.remove(1)
    print('Final List Is:', cc)
    if max(cc)-min(cc) == 0:
        print('YES')
        quit()

# If gap between highest/lowest is 1 and only one character
# has highest count, then we can subtract 1 and have parity
if cc.count(max(cc)) == 1 and max(cc) - min(cc) == 1:
    print('YES')
    quit()

print('NO')
