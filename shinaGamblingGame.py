import random
import time

def welcome():
  
  print("Welcome to Shina's minigames")
  time.sleep(2)
  
welcome()
time.sleep(3)
f = input("Is this your first time playing this Y/N:")
if f == "y" or f == "Y":
  print("""WELCOME TO SHINA'S Minigames! 
  As this is your first time gambling here are the rules
  
  1.You cannot gamble more than or equal 10000 as that is the maximum money this machine contains
  2.You must have at least 2 euro to play
  3. You must gamble what you currently have
  4.The game has imperfections but please let me know what I could improve on.

  5.Enjoy!!!!!!!!!!!""")
time.sleep(5)


def game():
    max_cashout = 10000
    money = 0
    g = random.randint(1,3)
    gamble = int(input("Enter how much u want to gamble:"))
    
    if gamble == 0:
      print("You dont have anything to gamble now...")
      exit()
    
    user_guess = int(input("Enter a guess between 1-3:"))
      #HERE IS THE MATHS PART
    if user_guess == g:
      print("Jackpot")
      money =  gamble + 10
      print("The ans was,",g)
      print("you are currently at",money,"euro")
        
    elif user_guess != g:
      print("Unlucky")
      money = gamble - 2
      print("The ans was,",g)
      print("you are currently at",money,"euro")
      
    elif money and gamble == 0:
      print("You dont have anything to gamble now...")
      exit()
      #CURRENTLY AT
    if money == max_cashout:
      print("You have won the game")
      exit()
    if str(user_guess) or str(gamble) == "x":
      exit()

time.sleep(1) 
choice = input("Do you want gamble or keep gambling Y/N:") 
while choice == "Y":
  game()
while choice == "N":
  print("Game OVER!")
  break