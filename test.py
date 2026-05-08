import random
import time
print("Hi my name is albert")
time.sleep(1)
name=input("what is your name?")
time.sleep(1)
print(f"hello {name}")
time.sleep(2)
print(f"{name} now let tell you the rules of this game you will be given 6 lives so lets see if you can win")
words=["book","school","python","computer","laptop","fat"]
secret=random.choice(words).lower()
time.sleep(1)
display= ["-"] * len(secret)
lives=6
while "-" in display and lives>0:
    print("\n" + " " .join(display))
    print(f"{lives} lives left")
    time.sleep(1)
    guess=input("what is your guess?").lower()
    if guess in secret:
        for i in range(len(secret)):
            if secret[i]==guess:
                display[i] = guess
        print ("Good job!")
    else:
        lives-=1
        print("Wrong guess!")
if "-" not in display:
     print(f"{name} congrats! you won")
else:
     print(f"{name} You lost")




























