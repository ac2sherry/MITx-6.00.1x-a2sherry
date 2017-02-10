def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '')
    return availableLetters
    	


secretWord = 'apple'
lettersGuessed = ['a','b','c','t','h','p','l']
print(getAvailableLetters(lettersGuessed))