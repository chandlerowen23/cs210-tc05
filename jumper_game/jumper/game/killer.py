import random

#class for printing out the parachute
class Killer():

    #initialize the attribute of the killer class
    def __init__(self):
        #list of words for jumper to randomize
        self.list_word =["house", "table", "rock", "guesser"]
        #random choice from the list of worder stored into word
        self.word = random.choice(self.list_word)


    #depending on how many fails or mistakes the print of the parachute will change
    def get_fails(self,fails):

        if fails >= 4:
            print("\n   X\n  /|\ \n  / \ \n \n^^^^^^^ ")

        elif fails >= 3:
            print("\n  \ / \n   0\n  /|\ \n  / \ \n \n^^^^^^^ ")

        elif fails >= 2:
            print("\n \   / \n  \ / \n   0\n  /|\ \n  / \ \n \n^^^^^^^ ")

        elif fails >= 1:
            print("\n /___\ \n \   / \n  \ / \n   0\n  /|\ \n  / \ \n \n^^^^^^^ ")

        elif fails == 0:
            print("\n  ___ \n /___\ \n \   / \n  \ / \n   0\n  /|\ \n  / \ \n \n^^^^^^^ ")



