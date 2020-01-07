'''
PEDAC Process

P - If there are any letters that show up more than once, you return false. If every letter shows up only once, you return true.

E - 'abcde' = True
    'aabcde' = False
    'abcddeFf' = False
    'Aa' = True
    '' = None

D - List (Dictionary)

A - 1. If the input is an empty string, return None
    2. Create empty dictionary
    3. Create a loop for the letters given
      3a. If the letter is not in the dictionary, put it in with a number 1
      3b. If the letter is already in the dictionary, add 1 to the count
    4. Check if any letter in the dictionary has more than one in their count
      4a. If any letter has more than one in their count, return False
    5. Return True
'''

