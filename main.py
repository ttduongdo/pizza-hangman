import random 
from graphics import *
import time 
import keyboard

def get_single_key():
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            return event.name


def random_word_from_library(word_list: list) -> str:
  """Choose a random word from the word list.
  :param word_list: (list) a list of words 
  :return: (str) a word
  """
  word_guess = random.choice(word_list)
  return word_guess
  
def clicked_how(u: Point) -> bool:
  """Check if the user clicks on the 'how to play' button.
  :param u: the coordinates of where the user clicks on the screen
  :return: (bool) True if the user has clicked on the 'how to play' button
  """
  if 130 <= u.getX() <= 425 and 100 <= u.getY() <= 200:
    return True
  else: 
    return False
def clicked_easy(u: Point) -> bool:
  """Check if the user clicks on the 'easy' button.
  :param u: the coordinates of where the user clicks on the screen
  :return: (bool) True if the user has clicked on the 'easy' button
  """
  if 90 <= u.getX() <= 210 and 300 <= u.getY() <= 345:
    return True
  else: 
    return False
def clicked_med(u: Point) -> bool:
  """Check if the user clicks on the 'medium' button.
  :param u: the coordinates of where the user clicks on the screen
  :return: (bool) True if the user has clicked on the 'medium' button
  """
  if 220 <= u.getX() <= 340 and 375 <= u.getY() <= 425:
    return True
  else:
    return False
def clicked_hard(u: Point) -> bool:
  """Check if the user clicks on the 'hard' button.
  :param u: the coordinates of where the user clicks on the screen
  :return: (bool) True if the user has clicked on the 'hard' button
  """
  if 340 <= u.getX() <= 460 and 300 <= u.getY() <= 345:
    return True
  else: 
    return False 
    
def easy_game(win):
  """Run the easy level game. Make the user guess a 9-letter word letter by letter and print out one hint. The user loses one slice of pizza per one wrong guess. The game stops when the user succeeds to guess the word or runs out of 6 wrong guesses.
  :param win: GraphWin
  """
  
  file = open("hints.txt", "r")
  lines = file.readlines()


  word_list = []
  hint_list = []
  for line in lines:
    word, hint = line.strip().split(",")
    word_list.append(word)
    hint_list.append(hint)
      
  file.close()
  win.setBackground("olive")
  
  paddle = Image(Point(250, 250), "i/paddle.png")
  paddle.draw(win)
    
  img = Image(Point(300, 150), "i/p1.png")
  img.draw(win)
      
  img2 = Image(Point(300, 350), "i/p2.png")
  img2.draw(win)
    
  img3 = Image(Point(385, 200), "i/p3.png")
  img3.draw(win)
    
  img4 = Image(Point(385, 300), "i/p4.png")
  img4.draw(win)
    
  img5 = Image(Point(215, 200), "i/p5.png")
  img5.draw(win)
    
  img6 = Image(Point(215, 300), "i/p6.png")
  img6.draw(win)
    
  txt = Text(Point(650, 400), "---------")
  txt.setTextColor("yellow")
  txt.setSize(30)
  txt.draw(win)
  
  word = random_word_from_library(word_list)
  i = word_list.index(word)
  word_hint = hint_list[i]
  print(f"Hint: {word_hint}")
  
  word_letter = []
  for letter in word: 
    word_letter.append(letter)
  
  blank = "---------" 
  print(blank)
   
  blank_letter = []
  for letter in blank: 
    blank_letter.append(letter)
  wrong_guesses = 0
  wrong_letter = [] 
  while wrong_guesses < 6 and "-" in blank_letter:
      user_letter = get_single_key().lower()
      while user_letter not in "abcdefghijklmnopqrstuvwxyz":
          print("Enter a valid letter")
          user_letter = get_single_key().lower()
      print(f"You entered: {user_letter}")
      if user_letter in word: 
        for i in range(len(word)):
          if user_letter == word[i]: 
            blank_letter[i] = user_letter
        blank_after = "".join(blank_letter)
        print(blank_after + "\n")
        txt.undraw()
        txt = Text(Point(650, 400), blank_after)
        txt.setTextColor("yellow")
        txt.setSize(30)
        txt.draw(win)
      else:
        if user_letter in wrong_letter:
          print("You already guessed this letter! Try a different one!\n")
        else:
          print("Nope, try again!\n")
          wrong_letter.append(user_letter)
          wrong_guesses += 1
          if wrong_guesses == 1:             
            img.undraw()
          elif wrong_guesses == 2:
            img3.undraw()
          elif wrong_guesses == 3:
            img4.undraw()
          elif wrong_guesses == 4:
            img2.undraw()
          elif wrong_guesses == 5:
            img6.undraw()
        
  
  if "-" not in blank_letter:
    print("\nYou got the word! The word was " + "\"" + word + "." + "\"")
  else:
    endgame_txt = Text(Point(300, 250), "game over")
    endgame_txt.setTextColor("gold")
    endgame_txt.setSize(30)
    endgame_txt.draw(win)
    img5.undraw()
    print("\nYou didn't get the word. The word was " + "\"" + word + "." + "\"")

def main_game(win):
  """Run the meidum level game. Make the user guess a 9-letter word letter by letter. No hint. The user loses one slice of pizza per one wrong guess. The game stops when the user succeeds to guess the word or runs out of 6 wrong guesses.
  :param win: GraphWin
  """
  file = open("library.txt", "r")
  lines = file.readlines()
  
  word_list = []
  for line in lines:
    word = line.strip(",\n")
    word_list.append(word)
    
  file.close()
  win.setBackground("olive")
  
  paddle = Image(Point(250, 250), "i/paddle.png")
  paddle.draw(win)
    
  img = Image(Point(300, 150), "i/p1.png")
  img.draw(win)
      
  img2 = Image(Point(300, 350), "i/p2.png")
  img2.draw(win)
    
  img3 = Image(Point(385, 200), "i/p3.png")
  img3.draw(win)
    
  img4 = Image(Point(385, 300), "i/p4.png")
  img4.draw(win)
    
  img5 = Image(Point(215, 200), "i/p5.png")
  img5.draw(win)
    
  img6 = Image(Point(215, 300), "i/p6.png")
  img6.draw(win)
    
  txt = Text(Point(650, 400), "---------")
  txt.setTextColor("yellow")
  txt.setSize(30)
  txt.draw(win)
  
  word = random_word_from_library(word_list)
  word_letter = []
  for letter in word: 
    word_letter.append(letter)
  
  blank = "---------" 
  print(blank)
  
  blank_letter = []
  for letter in blank: 
    blank_letter.append(letter)
  wrong_guesses = 0
  wrong_letter = [] 
  while wrong_guesses < 6 and "-" in blank_letter:
      user_letter = input("Enter one letter at a time: ")
      while user_letter not in ("qwertyuiopasdfghjklzxcvbnm"):
        user_letter = input("Enter a valid letter:")
      if user_letter in word: 
        for i in range(len(word)):
          if user_letter == word[i]: 
            blank_letter[i] = user_letter
        blank_after = "".join(blank_letter)
        print(blank_after + "\n")
        txt.undraw()
        txt = Text(Point(650, 400), blank_after)
        txt.setTextColor("yellow")
        txt.setSize(30)
        txt.draw(win)
      else:
        if user_letter in wrong_letter:
          print("You already guessed this letter! Try a different one!\n")
        else:
          print("Nope, try again!\n")
          wrong_letter.append(user_letter)
          wrong_guesses += 1
          if wrong_guesses == 1:             
            img.undraw()
          elif wrong_guesses == 2:
            img3.undraw()
          elif wrong_guesses == 3:
            img4.undraw()
          elif wrong_guesses == 4:
            img2.undraw()
          elif wrong_guesses == 5:
            img6.undraw()
        
  
  if "-" not in blank_letter:
    print("\nYou got the word! The word was " + "\"" + word + "." + "\"")
  else:
    endgame_txt = Text(Point(300, 250), "game over")
    endgame_txt.setTextColor("gold")
    endgame_txt.setSize(30)
    endgame_txt.draw(win)
    img5.undraw()
    print("\nYou didn't get the word. The word was " + "\"" + word + "." + "\"")
    
def hard_game(win):
  """Run the hard level game. Make the user guess as many 9-letter words as possible in 60 seconds. When the time runs out, the game stops. The user loses one slice of pizza per one wrong guess. 
  :param win: GraphWin
  """
  win.setBackground("olive")

  start_time = time.time() 
  flag = False
  correct_word = 0
  while not flag:
    file = open("library.txt", "r")
    lines = file.readlines()
    
    word_list = []
    for line in lines:
      word = line.strip(",\n")
      word_list.append(word)
      
    file.close()

    paddle = Image(Point(250, 250), "i/paddle.png")
    paddle.draw(win)
      
    img = Image(Point(300, 150), "i/p1.png")
    img.draw(win)
    img2 = Image(Point(300, 350), "i/p2.png")
    img2.draw(win)
    img3 = Image(Point(385, 200), "i/p3.png")
    img3.draw(win)
      
    img4 = Image(Point(385, 300), "i/p4.png")
    img4.draw(win)
      
    img5 = Image(Point(215, 200), "i/p5.png")
    img5.draw(win)
      
    img6 = Image(Point(215, 300), "i/p6.png")
    img6.draw(win)
      
    txt = Text(Point(650, 400), "---------")                
    txt.setTextColor("yellow")
    txt.setSize(30)
    txt.draw(win)
    
    word = random_word_from_library(word_list)
    word_letter = []
    for letter in word: 
      word_letter.append(letter)
    
    blank = "---------" 
    print(blank)
    
    blank_letter = []
    for letter in blank: 
      blank_letter.append(letter)
    wrong_guesses = 0
    wrong_letter = [] 
    while wrong_guesses < 6 and "-" in blank_letter:
        user_letter = input("Enter one letter at a time: ")
        while user_letter not in ("qwertyuiopasdfghjklzxcvbnm"):
          user_letter = input("Enter a valid letter:")
        if user_letter in word: 
          for i in range(len(word)):
            if user_letter == word[i]: 
              blank_letter[i] = user_letter
          blank_after = "".join(blank_letter)
          print(blank_after + "\n")
          txt.undraw()
          txt = Text(Point(650, 400), blank_after)
          txt.setTextColor("yellow")
          txt.setSize(30)
          txt.draw(win)
        else:
          if user_letter in wrong_letter:
            print("You already guessed this letter! Try a different one!\n")
          else:
            print("Nope, try again!\n")
            wrong_letter.append(user_letter)
            wrong_guesses += 1
            if wrong_guesses == 1:             
              img.undraw()
            elif wrong_guesses == 2:
              img3.undraw()
            elif wrong_guesses == 3:
              img4.undraw()
            elif wrong_guesses == 4:
              img2.undraw()
            elif wrong_guesses == 5:
              img6.undraw()
          
  
    if "-" not in blank_letter:
      print("\nYou got the word! The word was " + "\"" + word + "." + "\"")
      correct_word += 1
      txt.undraw()
    else:
      #endgame_txt = Text(Point(300, 250), "game over")
      #endgame_txt.setTextColor("gold")
      #endgame_txt.setSize(30)
      #endgame_txt.draw(win)
      img5.undraw()
      print("\nYou didn't get the word. The word was " + "\"" + word + "." + "\"")
      txt.undraw()
      
    if time.time() - start_time > 60:
      flag = True
      print("Time's up!")
      print(f"You got {correct_word} correct words.")
      break
    
def main():

  play_again = ("Yy")
  
  while "Y" in play_again or "y" in play_again:
    win = GraphWin("Pizza", 800, 500)
    
    # c = Circle(Point(300,250), 150)
    # c.setFill("goldenrod")
    # c.draw(win)
  
    win.setBackground("dark salmon")
    c4 = Image(Point(275, 250), "i/Pizza.png")
    c4.draw(win)
    c = Image(Point(150, 325), "i/Button.png")
    c.draw(win)
    c5 = Image(Point(275, 155),"i/Button.png2.png")
    c5.draw(win)
    
    c2 = Image(Point(280, 400), "i/Button.png")
    c2.draw(win)
  
    c3 = Image(Point(400, 325), "i/Button.png")
    c3.draw(win)
    
    txt1 = Text(Point(150, 325), "easy")
    txt1.draw(win)
    txt2 = Text(Point(280, 400), "medium")
    txt2.draw(win)
    txt3 = Text(Point(400, 325), "hard")
    txt3.draw(win)
    txt4 = Text(Point(275, 155), "how to play")
    txt4.setSize(25)
    txt4.draw(win)
  
  
    u = win.getMouse()
    if clicked_how(u) == True:
      print("\n~~~Welcome to SLICE EATER! To play, guess one letter at a time until you have correctly guessed all the letters in the 9-letter word. But be careful - for every wrong guess, a slice of pizza disappears. Guess the word before your pizza is gone!~~~\n")
      print("easy: guess the word with a hint")
      print("medium: guess the word without any hint")
      print("hard: guess as many words as you can in 60 seconds")
      continue
    elif clicked_easy(u) == True:
      c.undraw()
      c4.undraw()
      c5.undraw()
      c2.undraw()
      c3.undraw()
      txt1.undraw()
      txt2.undraw()
      txt3.undraw()
      txt4.undraw()
      easy_game(win)
    elif clicked_med(u) == True:
      c.undraw()
      c4.undraw()
      c5.undraw()
      c2.undraw()
      c3.undraw()
      txt1.undraw()
      txt2.undraw()
      txt3.undraw()
      txt4.undraw()
      main_game(win)
    elif clicked_hard(u) == True:
      c.undraw()
      c4.undraw()
      c5.undraw()
      c2.undraw()
      c3.undraw()
      txt1.undraw()
      txt2.undraw()
      txt3.undraw()
      txt4.undraw()
      hard_game(win)
  
    
    play_again = input("\nDo you want to play again? (Y or y for yes)")
  

  print("\nThank you for playing!")
  
    
if __name__ == "__main__":
  main()
