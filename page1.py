playerhealth = 35
strmodifier = 1

def battlereset():
    global enemyhealth
    global enemystr
    enemyhealth = randint(10, 30)
    enemystr = randint(2, 4)


def playerchoice():
    global enemyhealth
    global enemystr
    global strmodifier
    global playerhealth
    playerchoice = input("Would you like to Attack or Heal?")
    if playerchoice.lower() == "attack":
        damage = randint(2, 4) * strmodifier
        enemyhealth = enemyhealth - damage
        print("You dealt " + str(damage) + " damage")
        print("SOMETHING has " + str(enemyhealth) + " health remaining")
    elif playerchoice.lower() == "heal":
        healchance = randint(1, 4)
        if healchance > 2:
            heal = playerhealth * .25
            playerhealth = playerhealth + heal
            print("You have been healed for " + str(heal) + " health")
            print("You now have " + str(playerhealth) + " Health")
        else:
            print("Your heal has failed.")
    else:
        print("Please enter a valid action.")
        playerchoice()
    enemychoice()


def enemychoice():
    global playerhealth
    global enemyhealth
    enemychoice = randint(1, 4)
    if enemychoice == 1 or 2:
        damage = enemystr + randint(1, 3)
        playerhealth = playerhealth - damage
        print("SOMETHING did " + str(damage) + " damage.")
        print("You have " + str(playerhealth) + " health remaining.")
    elif enemychoice == 3 or 4:
        heal = enemystr - 4
        heal = abs(heal)
        enemyhealth = enemyhealth + (3 * heal)
        print("SOMETHING has healed for " + str(heal) + " health")
        print("SOMETHING now have " + str(enemyhealth) + " health")
    battlego()


def battlego():
    global playerhealth
    global enemyhealth
    if playerhealth < 0:
        print(
            "ḭ̵̓̊s̸̜͠ ̵̦͂̃i̷̮̎͝t̸̬̎̋ ̶̧̜̃d̵̬̣͝e̷̪͋a̸͚̜̽̚t̷̬͐̊h̷̪̄ ̷̧̛̳̓i̴͕̅̀͜f̸̨̄͘ ̶͚̞͒y̴̺̍͝ó̸͓ǔ̵̢͉'̵̧̒͋ͅr̵̫͒e̸̫̓ ̸͓̏a̴̰̬͝l̶̝̊̈́͜r̶̼̞̄́e̷̮̾͗â̶͔̝͂ḑ̶͕̓͠y̵͔͋̓ ̷̗̂̈́g̸̟͈͂́o̵̼̱̎n̷̨̿e̵̘͊̓?̴̢̲̃̂"
        )
        again = input("Try again? (Y/N?)")
        while again.lower() != "y" and again.lower() != "n":
            print("Please enter one of the listed letters.")
        if again.lower() != "y":
            newbattle()
        elif again.lower() != "n":
            start()
        return
    elif enemyhealth < 0:
        print("Congratulations.")
        win()
    else:
        playerchoice()


def newbattle():
    battlereset()
    print("SOMETHING has " + str(enemyhealth) + " health")
    print("\nYou have " + str(playerhealth) + " health.")
    battlego()