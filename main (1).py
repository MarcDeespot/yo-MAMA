import random
whichStart = random.randrange(1, 6)
whichMiddle = random.randrange(1, 6)
whichEnd = random.randrange(1, 6)
def meanMama():
    if whichStart == 1:
        print('Yo mama so fat ', end='')
    elif whichStart == 2:
        print('Yo mama so ugly ', end='')
    elif whichStart == 3:
        print('Yo mama so short ', end='')
    elif whichStart == 4:
        print('Yo mama so old ', end='')
    elif whichStart == 5:
        print('Yo mama so stupid ', end='')
    else:
        print('Error!')
    if whichMiddle == 1:
        print('she fell off a cliff and ', end='')
    elif whichMiddle == 2:
        print('she ate a cheeseburger and ', end="")
    elif whichMiddle == 3:
        print('she played the piano and ', end="")
    elif whichMiddle == 4:
        print('she ran and ', end='')
    elif whichMiddle == 5:
        print('she combed a bear and ', end='')
    else:
        print('Error!')
    if whichEnd == 1:
        print('the moon exploded!', end='')
    elif whichEnd == 2:
        print('she pooped her pants!', end='')
    elif whichEnd == 3:
        print('she became the god of marshmallows!', end='')
    elif whichEnd == 4:
        print('earth radiated into nothing!', end='')
    elif whichEnd == 5:
        print('golf-ball sized hail established a Republic in Russia!', end='')
    else:
        print('Error!')
def niceMama():
    if whichStart == 1:
        print('Yo mama so fat ', end='')
    elif whichStart == 2:
        print('Yo mama so ugly ', end='')
    elif whichStart == 3:
        print('Yo mama so short ', end='')
    elif whichStart == 4:
        print('Yo mama so old ', end='')
    elif whichStart == 5:
        print('Yo mama so stupid ', end='')
    else:
        print('Error!')
    if whichMiddle == 1:
        print('she fell off a cliff and ', end='')
    elif whichMiddle == 2:
        print('she ate a cheeseburger and ', end="")
    elif whichMiddle == 3:
        print('she played the piano and ', end="")
    elif whichMiddle == 4:
        print('she ran and ', end='')
    elif whichMiddle == 5:
        print('she combed a bear and ', end='')
    else:
        print('Error!')
    if whichEnd == 1:
        print('she cured world hunger!', end='')
    elif whichEnd == 2:
        print('she established a loving society.', end='')
    elif whichEnd == 3:
        print('she fixed being left on seen.', end='')
    elif whichEnd == 4:
        print('she caused an ethical and moral dilemma in society thus establishing an equal playing fields for all '
              'individuals, given that nobody is perfect and each fault is merely a reminder that we\'re all human.',
              end='')
    elif whichEnd == 5:
        print('she helped an elderly woman cross the street.', end='')
    else:
        print('Error!')
meanMama()
print('')
niceMama()