import random

# Define class here
class Wordle:
    word_bank = ['brave', 'brake','tiger', 'lions']
    num_wins = 0
    num_losses = 0
    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.word = random.choice(Wordle.word_bank)
        self.guesses = []

    def __str__(self):
        final_string = ''
        for guess in self.guesses:
            my_guess = ''
            for i in range(len(guess)):
                result = 'r'
                if guess[i] in self.word:
                    result = 'y'
                    if guess[i] == self.word[i]:
                        result = 'g'
                my_guess += guess[i].upper() + '(' + result + ')' 
            final_string += my_guess + '\n'
        return f'{final_string}{self.num_guesses} guesses remaining'

    def make_guess(self, guess):
        if len(guess) != 5:
            print('Guess must be exactly 5 letters. Try again')
            return False
        if len(set(guess)) != len(guess): 
            print("Guess must contain unique letters only. Try again")
            return False 
        self.guesses.append(guess.lower())
        if guess.lower() == self.word.lower():
            print("You win!")
            Wordle.num_wins = Wordle.num_wins + 1
            self.num_guesses = self.num_guesses - 1 
            return True
            
        if self.num_guesses == 0:
            print('You lose!')
            Wordle.num_losses += 1
            return True
        self.num_guesses = self.num_guesses - 1 
        return False

# No need to touch code below this line unless you
# would like to play with different settings. It allows
# you to interact with an instance of your class.
def run_program():
    play_again = 'y'
    while play_again == 'y':
        wordle_game = Wordle(6)
        print(wordle_game)
        game_over = False
        while not game_over:
            guess = input('What is your guess? ')
            game_over = wordle_game.make_guess(guess)
            print(wordle_game)
        print("Wins: {}, Losses: {}".format(Wordle.num_wins, Wordle.num_losses))
        print()
        play_again = input("Play again(y/n)? ")
        print()
    print("All done!")

if __name__ == "__main__":
    run_program()
