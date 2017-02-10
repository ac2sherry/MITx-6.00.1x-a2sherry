def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in lettersGuessed:
    	if letter in secretWord:
    		secretWord = secretWord.replace(letter, '')
    return len(secretWord) == 0
    	


secretWord = 'apple'
lettersGuessed = ['a','b','e','c','t','h','p','l']

print(isWordGuessed(secretWord, lettersGuessed))