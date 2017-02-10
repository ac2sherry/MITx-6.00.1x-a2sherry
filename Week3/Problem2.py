def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWordList = ['_']*len(secretWord)
    for letter in lettersGuessed:
    	for idx in range(len(secretWord)):
            if letter == secretWord[idx]:
                guessedWordList[idx] = letter
    guessedWord = ''.join(guessedWordList)
    return guessedWord
    	


secretWord = 'apple'
lettersGuessed = ['a','b','c','t','h','p','l']
print(getGuessedWord(secretWord, lettersGuessed))