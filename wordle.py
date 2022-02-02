class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class wordle:
    def __init__(self, word, guesses=6):
        self.guesses = []
        self.word = word.upper()
        self.maxguesses = guesses

        self.letterDict = {}
        for letter in self.word:
            if letter in self.letterDict:
                self.letterDict[letter] += 1
            else:
                self.letterDict[letter] = 1
        self.invalid = {}
        self.valid = {}
    
    def check_game_over(self):
        # Check if you are out of guesses
        if len(self.guesses) == self.maxguesses:
            return True
        else:
            # Check if the word has been guessed
            if self.check_word():
                return True
            return False
    
    def check_win(self):
        # Check if the last guess was correct
        if len(self.guesses)>0:
            last_word = self.guesses[-1]
            last_word = ''.join(last_word)
            if last_word == self.word:
                return True
        return False

    def guess(self, guess):
        if len(self.guesses) == self.maxguesses:
            print("You are out of guesses")
            return False
        if self.check_win():
            print("You already won the game")
            return False

        # Check if the guess is valid
        if len(guess) != len(self.word):
            print("Your guess is not " + str(len(self.word)) + " letters long.")
            return False
        letterDict = self.letterDict.copy()
        guess = guess.upper()
        if guess in self.guesses:
            print("You already guessed that word!")
            return False
        wordString = ''
        valid = True
        for i, letter in enumerate(guess):
            if letter in self.invalid:
                print("Letter " + str(letter) + " was already said to be invalid!")
                return False
            if self.word[i] == letter:
                wordString = wordString + bcolors.OKGREEN + letter + bcolors.ENDC
                letterDict[letter] = letterDict[letter] - 1
                if letterDict[letter] == 0:
                    letterDict.pop(letter)
            elif letter in letterDict:
                wordString = wordString + bcolors.WARNING + letter + bcolors.ENDC
                letterDict[letter] = letterDict[letter] - 1
                if letterDict[letter] == 0:
                    letterDict.pop(letter)
                valid = False
            else:
                wordString = wordString + bcolors.FAIL + letter + bcolors.ENDC
                self.invalid[letter] = letter
                valid = False
        
        self.guesses.append(guess)
        if valid:
            print(wordString)
            print("You guessed correctly!")
            return True
        print(wordString)
        print("Try again!")
        return False

word = wordle("hello")
word.guess("false")
word.guess("false")
word.guess("helli")
word.guess("helli")
word.guess("helli")
word.guess("helli")

word.guess("hello")
word.guess("hello")
