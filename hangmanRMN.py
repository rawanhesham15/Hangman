from random import choice
words = ['lion','rabbit','dog','cat','pig','chicken','fox']
word = choice(words)
guessed_letters=[]
displayed_word="_"*len(word)

hangmanStages = [
    """ 
    -----
    |   |
        |
        |
        |
    ======
    """,
""" 
    -----
    |   |
    O   |
        |
        |
    ======
    """,
""" 
    -----
    |   |
    O   |
    |   |
        |
    ======
    """,
    """ 
    -----
    |   |
    O   |
  / | \ |
        |
    ======
    """,
    """ 
    -----
    |   |
    O   |
  / | \ |
    |   |
    ======
    """,
    """ 
    -----
    |   |
    O   |
  / | \ |
    |   |
   / \  |
    ======
    """,
        ]
print ("_"*len(word))
mistakes = 0
def guess_letter():
    global mistakes,displayed_word
    guess = input("enter your guess letter: ")
    while guess in guessed_letters:
        guess = input("enter your guess letter: ")
    guessed_letters.append(guess)

    for i in range(0,len(word)):
        if guess == word[i]:
            displayed_word = displayed_word[:i]+guess+displayed_word[i+1:]
            print (displayed_word)
    if guess not in word:
        print("wrong guess,try again!")

        print(hangmanStages[mistakes])
        mistakes += 1

while mistakes < 6:
    guess_letter()
    if displayed_word == word:
        print("you win!")
        break



