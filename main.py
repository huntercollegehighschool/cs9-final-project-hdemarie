"""
Name: Demarie Hao
Name of Project: CS9 Final Project: LIMBO
"""

"---combat commands---"
from random import randint

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
    playerc = input("Would you like to Attack or Heal?")
    if playerc.lower() == "attack":
        damage = randint(2, 4) * strmodifier
        enemyhealth = enemyhealth - damage
        print("You dealt " + str(damage) + " health.")
        print("SOMETHING has " + str(enemyhealth) + " health remaining")
    elif playerc.lower() == "heal":
        healchance = randint(1, 4)
        if healchance > 2:
            heal = playerhealth * .25
            heal = heal - (heal%1)
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
        playerhealth = float(playerhealth - damage)
        print("SOMETHING did " + str(damage) + " damage.")
        print("You have " + str(playerhealth) + " health remaining.")
    elif enemychoice == 3 or 4:
        heal = enemystr - 4
        heal = abs(heal)
        enemyhealth = (enemyhealth + (3 * heal))
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
        if again.lower() == "y":
            start()
        elif again.lower() == "n":
            end()
        return
    elif enemyhealth < 0:
        print("Congratulations.")
        win()
    else:
        playerchoice()


def newbattle():
    battlereset()
    print("SOMETHING has " + str(enemyhealth) + " health.")
    print("You have " + str(playerhealth) + " health.")
    battlego()


"---start---"


def start():
    global playerhealth
    playerhealth = 35
    print(
        "You open your eyes to see yourself in an empty subway station. How did you get here?"
    )
    input()
    print(
        "You see a train pulling into the station. To your right is a staircase leading upwards. To your left is a phone booth."
    )
    choice = input(
        "\nWhere do you want to go? Enter T for train, S to climb upstairs, or P to examine the phone booth."
    )
    while choice.lower() != "t" and choice.lower() != "s" and choice.lower(
    ) != "p":
        print("Please enter one of the listed letters.")
        choice = input(
            "\nWhere do you want to go? Enter T for train, S to climb upstairs, or P to examine the phone booth."
        )
    if choice.lower() == "t":
        train()
    elif choice.lower() == "s":
        upstairs()
    elif choice.lower() == "p":
        phone()


def win():
    print(
        "You have defeated SOMETHING. A note lays where SOMETHING was.\n You pick it up. It reads \"--9-3-1-.\""
    )
    start()


"---choices---"


def train():
    print(
        'You enter the train as the doors open. A loudspeaker clicks on and announces,\"It is not your time. Please exit the train.\"'
    )
    person = input(
        "\nA figure sits in the corner of the train. Enter E to exit the train. Enter C to confront the figure."
    )
    while person.lower() != "e" and person.lower() != "c":
        print("Please enter one of the listed letters.")
        person == input(
            "\nA figure sits in the corner of the train. Enter E to exit the train, or enter C to confront the figure."
        )
    if person.lower() == "e":
        start()
    elif person.lower() == "c":
        confrontation()


def confrontation():
    print(
        "You approach the figure looming the corner. Two beady eyes stare back at you."
    )
    newbattle()


"-----"


def upstairs():
    print(
        "You walk upstairs. The dull buzz of the station lights rings in your ear as you walk. When do these stop?"
    )
    input()
    print(
        "\nYou spot the top of the stairs after what feels like days. A light shines through the bars guarding the exit. You glance around and see a post-it stuck on the wall."
    )
    note = input("\nDo you take the post-it? (Y/N)")
    while note.lower() != "y" and note.lower() != "n":
        print("Please enter (Y/N).")
    if note.lower() == "y":
        ynote()
    elif note.lower() == "n":
        nnote()


def ynote():
    print("You take the post-it on the wall. \nIt reads 12--1-2-5.")
    input()
    print(
        "The shadows around seem to grow larger as you stare at the note. You look up to see two white eyes glaring at you."
    )
    newbattle()


def nnote():
    white = input(
        "You look away from the post-it note. \nYou look through the bars and see nothing but white. Examine? (Y/N)"
    )
    while white.lower() != "y" and white.lower() != "n":
        print("Please enter (Y/N).")
    if white.lower() == "y":
        print(
            "You stare into a blank white void. A ringing sounds through your ears as fireworks of all different colors seem to suddenly paint the blank sheet of paper and no, no no---"
        )
        downstairs()
    elif white.lower() == "n":
        print("You take a glance and simply look away.")
        downstairs()


def downstairs():
    bars = input(
        "You look around again. Enter P to examine the post-it. Enter D to leave the stairwell."
    )
    while bars.lower() != "p" and bars.lower() != "d":
        print("Please enter one of the listed letters.")
    if bars.lower() == "p":
        ynote()
        input()
        print(
            "\nYou tear your eyes away from the bars and look down the stairs. The shadows around seem to grow larger as you stare at the note. You look up to see two white eyes glaring at you."
        )
        newbattle()
    elif bars.lower() == "d":
        print(
            "You tear your eyes away from the bars and look down the stairs. The shadows around seem to grow larger as you stare at the note. You look up to see two white eyes glaring at you."
        )
        newbattle()


"----"


def phone():
    print(
        "You arrive at the phonebooth. The phone hangs on the wall silently.")
    call = input(
        "\nEnter N to enter in the code. Enter L to leave the phone booth.")
    while call.lower() != "n" and call.lower() != "l":
        print("Please enter one of the listed letters.")
    if call.lower() == "n":
        code()
    elif call.lower() == "l":
        start()


def code():
    code = input("Please enter the code.")
    if code == "12913215":
        print("The phone rings. Once. Twice. Thrice.")
        input()
        print(
            "\"One day you'll escape limbo,\" a voice rings. \"Today is not that day. You must repent for the atrocities committed in your past life. Do you remember the dynamite?.\""
        )
        input()
        print(
            "The end tone buzzes in your ear. You look out the glass of the phone booth and see Something. It looms over you until your vision is taken over by darkness."
        )
        input()
        end()
    else:
        incorrect = input(
            "The phone buzzes, and a voice sounnds. \"That is incorrect. Please try again.\" Enter T to try again. Enter L to leave the phone booth."
        )
        while incorrect.lower() != "t" and incorrect.lower() != "l":
            print("Please enter one of the listed letters.")
        if incorrect.lower() == "t":
            code()
        elif incorrect.lower() == "l":
            start()


def end():
    again = input("Thanks for playing! Play again? (Y/N)")
    while again.lower() != "y" and again.lower() != "n":
        print("Please enter (Y/N).")
    if again.lower() == "y":
        start()
    elif again.lower() == "n":
        print(":)")


print(start())
