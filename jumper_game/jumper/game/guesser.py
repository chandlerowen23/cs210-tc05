import random

class Guesser():

    def __init__(self):
        self.list_word =["house", "table", "rock", "guesser"]
        self.word = random.choice(self.list_word)
        self.display = ""
        self.first_hint = ""
        self.fails = 0

    def get_hint(self):
        self.display = '_' * len(self.word)
        self.first_hint = self.display
        #print(self.word)
        return self.first_hint

    def do_guess(self,letter):

        # replace underscore with the letter found in the word
        i = 0
        if letter in self.word:
            while self.word.find(letter, i) != -1:
                i = self.word.find(letter, i)
                self.display = self.display[:i] + letter + self.display[i + 1:]
                i += 1
        else:
            self.fails += 1

        return self.display
    
    #returns fails from do_guess
    def get_back_fails(self):
        return self.fails

    #returns word from do_guess
    def get_back_word(self):
        return self.word



