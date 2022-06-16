"""
Name(s): Lauren and Nile
Name of Project: The wayward life
"""
import os 
import time 

def start():
  print("Your house has gone up in flames. You can choose to save A, B, or C\n")
  choice =  input("Enter A for a baby, B for a book of all the answers you have ever wondered, or C for a dog: \n")
  if choice == "A":
    choiceA()
  elif choice == "B":
    choiceB()
  elif choice == "C":
    choiceC()
def choiceA():
  print("You've chosen to save the baby. You hear the book burn to a crisp and you struggle to ignore the yelps of a dying dog. You can either raise the child as your own, leave it on the steps of a church, or return to the start.\n")
  choice = input("Enter R for raise the child as your own, L for leave it on the steps of a church, or S to return to the start.\n")
  if choice == "R":
    raisethechild()
  elif choice == "L":
    stepsofthechurch()
  elif choice == "S":
    time.sleep(2)
    os.system("clear")
    start()
def raisethechild():
  print("You raise the child as your own and they grow up to be a billionare. You earned the Ride or Die award.\n")
  time.sleep(2)
  os.system("clear")
  start()
def stepsofthechurch():
  print("You leave the child on the steps and someone steals them away. The guilt and regret slowly eats away at your heart until you die.\n")
  time.sleep(2)
  os.system("clear")
  start()
def choiceB():
  print("You've chosen to save the book that answers all of the question you've even wondered. You hear the wails of the baby as the fire consumes it and the howls of the dog as it burns. You can either decide to read the book, hide it so no one can ever find it (nobody should have that kind of power), or return to the start.\n")
  choice = input("Enter D to read the book, H for hide it away, or S to return to the start.\n")
  if choice == "D":
    readthebook()
  elif choice == "H":
    hideitaway()
  elif choice == "S":
    time.sleep(2)
    os.system("clear")
    start()
def readthebook(): 
  print("You open the book and read the first page. As you read more and more, you find yourdelf unable to stop. The amount of knowledge is consuming you, and soon it is too late to save you. You die a lonely death, with your only company being the very book that killed you.\n")
  time.sleep(3)
  os.system("clear")
  start()
def hideitaway():
  print("You bury the book in an abandoned graveyard and no one ever sees it again. You are happy that no one will ever hold that type of power, but spend the rest of your life with a burning curiosity. What was in the book? Where would you be now if you had read it? You will never know.\n")
  time.sleep(3)
  os.system("clear")
  start()
def choiceC():
  print("You've chosen to save the dog. You hear the desperate crying of the baby and you can smell the burnt pages of the book. You can either bring the dog home, give it to your friend, or return to the start.\n")
  choice = input("Enter M to bring the dog home, G for give it to your friend, or S to return to the start.\n")
  if choice == "M":
    bringthedoghome()
  elif choice == "G":
    giveittoyourfriend()
  elif choice == "S":
    time.sleep(2)
    os.system("clear")
    start()
def bringthedoghome():
  print("You bring the dog home and care for it as best as you can. You have now earned a loyal compainion who will be your friend until the end of it's days.\n")
  time.sleep(3)
  os.system("clear")
  start()
def giveittoyourfriend():
  print("You surprise your friend with the dog and they are immensely grateful. However, one night, when your friend is asleep, the dog bites her on the leg. Later, it turns out the dog had rabies and thus causes a huge finacial strain on your friend, causing her to drop your friendship and abandon you.\n")
  time.sleep(3)
  os.system("clear")
  
start()
