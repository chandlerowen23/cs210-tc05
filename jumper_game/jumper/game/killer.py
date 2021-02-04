import random

class Killer():

    def __init__(self):
        self.list_word =["house", "table", "rock", "guesser"]
        self.word = random.choice(self.list_word)


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



