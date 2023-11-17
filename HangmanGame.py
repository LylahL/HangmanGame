import random


class HangmanGame:
    def __init__(self, word):
         self.selected_word = word
         self.wrong_letters = set()
         self.n_correct = 0  # number of correct guesses
         self.n_incorrect = 0  # number of incorrect guesses
         self.n_total = 0 # number of total guesses
         self.cur_display = []
         self.n = len(self.selected_word)
         self.pic = [] # imagine this is a pic of a person being hanged
        
        
    def greetings(self):
        """greets the player"""
        print("Hello there, welcome to hangman! Guess right or get hang:)")
    
    def current_display(self):
         """initialize current display"""
         self.cur_display = ["*"] * self.n 
    
    def current_display_helper(self):
        """Unfortunately directly modify letters in a string is tricky
        so I changed the display into a list
        this function helps change it back into a string"""
        return ''.join(self.cur_display)

    
    def check_if_letter_in_word(self, letter):
        "this function check if the letter guessed is in the word"
        for i in range(0, self.n):
                if letter == self.selected_word[i]: # if correct guess
                    if self.cur_display[i] == "*": # handles when there are multiple same letters in same word.
                        self.cur_display[i] = letter
                        return True
        return False


    def guessing(self):
        """promt guess, check if guessed letter in selected word, display message"""
        while self.current_display_helper() != self.selected_word: # Can't stop untill guess right
            letter = input("Please guess a letter: ")
            if self.check_if_letter_in_word(letter):# if correct guess
                    print(self.current_display_helper())
                    self.n_correct += 1
                    self.n_total += 1
            else: # if incorrect guess 
                self.wrong_letters.add(letter)
                print(f"Opps! Wrong guess. These are the letters that aren't in the word:{self.wrong_letters}")
                self.n_incorrect += 1
                self.n_total += 1
                self.draw_bodypart()
            print(f"You have guessed {self.n_total} times. \n --{self.n_correct} times right, {self.n_incorrect} times wrong.")
    
    def end_of_game(self):
        """when the word is guessed, print messages"""
        print(f"Hurray! You have correctly guessed the word, and you have took {self.n_total} tries.")

    def play(self):
        """This function organizes the order of functions"""
        self.greetings()
        self.current_display()
        self.guessing()
        self.end_of_game()

    def draw_bodypart(self):
        """draw a new body part for each incorrect guess
            I tried my best...
        """
        bodyparts = ["head", "torso", "left arm", "right arm", "left leg","right leg"]
        if self.n_incorrect > len(bodyparts): # checks if there're still enough body parts to draw
            print("Too many incorrect guesses, not enough body parts to draw! \nWell, you've successfully hanged a person")
        else:
            cur_bodypart = bodyparts[self.n_incorrect - 1] # body part that will be hang
            self.pic.append(cur_bodypart)
            print(f"This is the new body part just got hanged: {cur_bodypart}.\nthe Whole picture looks like this: {self.pic} hanging on the gallow ")

def select_word(word_list):
    """this function selects a different word from the wordList for each time called"""
    selected_word = random.choice(word_list)
    word_list.remove(selected_word)
    return selected_word


def game_helper(word_list):
    """This function create a class to start a round
    and ask the player if they want another round"""
    selected_word = select_word(word_list)
    first_round = HangmanGame(selected_word)
    first_round.play()

    while True:
        answer = input("Hey, wanna play again? ((0) Yes, let's go! /(1) No, I quit.) \n Instructions: Please enter 0 or 1: ")
        if answer == "0":
            selected_word = select_word(word_list) # This time it will select another word
            another_round = HangmanGame(selected_word)
            another_round.play()
        elif answer == "1":
            print("Thanks for playing, see you next time!")
            break
        else:
            print("I don't know what you mean. Read the Instructions, '0' means yes, '1' means no.")
            


    


def main():
    word_list = ["office", "of", "information","technology","computer","science", "faith","god","education", "pray"]
    game_helper(word_list)
    




if __name__ == "__main__":
    main()