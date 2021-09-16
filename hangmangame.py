import random
words=['View','Code','Tools','kitchen','Ground','Large','Margin','Window']
choose_word=random.choice(words)  #randomly choose the word from words list
word= choose_word.upper() #converting to upper case

def gameplay(word):
   intial_word = "_" * len(word) #displaying the word intially with underscores
   user_guessed= False
   user_guessed_letters =[]
   tries = 6  #no of parts left to be drawn of hangman
   print("Welcome to Hangman :) ")
   print(intial_word)
   print("\n")
   while not user_guessed and tries>0:
       guess_input = input("Enter a Letter")
       guess=guess_input.upper()

       if guess.isalpha() and len(guess)==1:
           if guess in user_guessed_letters:
               print("you have already guessed the letter")
           elif guess not in word:
               print("Sorry wrong word")
               tries -= 1
               user_guessed_letters.append(guess)
           else:

               print("Woohoo!You guessed it correct.")
               user_guessed_letters.append(guess)
               word_to_list=list(intial_word)
               indices = [i for i, letter in enumerate(word) if letter == guess]
               for index in indices:
                   word_to_list[index] = guess
               intial_word = "".join(word_to_list)
               if "_" not in intial_word:
                   user_guessed = True
       else:
           print("Not a valid guess")
       print("Number of tries left",tries)
       print(intial_word)
       print(display_hangman(tries))
       print("\n")
   if user_guessed:
        print("Congrats,You won!")
   else:
        print("You ran out of tries,The word is "+word)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |     / \
                   |
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |     / 
                   |
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |    
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |    
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |     
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    gameplay(word)
    while input("Play again?y/n").upper()=="Y":
        gameplay(word)

if __name__=="__main__":
    main()



