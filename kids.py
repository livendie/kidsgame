weapon = False
#code for cavernStart room
def cavernStart():
    directions = ["left","right","forward"]
    print("You push the bookshelf out of the way and notice a opening into a cavern behind it. You are just small enough to")
    print("fit through. You get on your hands and knees and enter the cavern. Inside the cavern, you enter a room no bigger")
    print("than a couple beds wide and just tall enough for you to stand up in. In front of you and on both sides of you,")
    print("you see other openings.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward\n")
        userInput = input("> ")
        if userInput == "left":
            weapon11()
        elif userInput == "right":
            empty12()
        elif userInput == "forward":
            monster12()
        else:
            print("Please enter a valid option.")

#code for weapon11 room
def weapon11():
    directions = ["forward","right","backward"]
    global weapon
    print("\nin front if you is a wall with a picture on it\n")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/right/backward\n")
        userInput = input("> ")
        if userInput == "forward":
            print("You examine the picture and find that there is something behind it. It's a sword\n")
            weapon = True
            print("Options: continue/back\n")
            userInput = input("> ")
            if userInput == "continue":
                monster11()
            elif userInput =="back":
                cavernStart()
            else:
                print("Please enter a valid option")
        elif userInput == "right":
            monster11()
        elif userInput == "backward":
            cavernStart()
        else:
            print("Please enter a valid option")

#code for monster11 room
def monster11():
    actions = ["fight","flee"]
    global weapon
    print("\nThere is a shadowy creature hiding behind a rock. He jumps out at you bearing teeth as white as ivory, and")
    print("hisses at you.\n")
    userInput = ""
    while userInput not in actions:
        print ("Options: fight/flee\n")
        userInput = input("> ")
        if userInput == "fight":
            if weapon:
                print("\nYou slay the vile beast and continue on to the next room. Congratulations on your conquest!\n")
                gold12()
            else:
                print("\nYou are slain by the vile beast and rot there for eternity. Sucks to suck.")
            quit()
        elif userInput == "flee":
            print("\nYou are slain by the vile beast and rot there for eternity.")
            quit()
        else:
            print("Please enter a valid option")

#code for gold12 room
def gold12():
    directions = ["climb","back"]
    print("\nAs you enter the room, you see a gold coin on the floor. In front of you is a ladder to climb.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: climb/back\n")
        userInput = input("> ")
        if userInput == "climb":
            print("\nYou have crawled into the outhouse at the lookout and are all covered in poop!\n")
            quit()
        elif userInput == "back":
            monster11()
        else:
            print("Please enter a valid option")

#code for monster12 room
def monster12():
    actions = ["fight","flee"]
    global weapon
    print("\nYou walk into a darkly lit room and see a glowing on the floor. You pick it up and realize that it's a glowing")
    print("enchanted dagger. Enscribed on it, are the words, \"lost are many without a light.\n")
    weapon = True
    print("There is a shadowy creature hiding behind a rock. He jumps out at you bearing teeth as white as ivory, and hisses")
    print("at you.\n")
    userInput = ""
    while userInput not in actions:
        print ("Options: flee/fight\n")
        userInput = input("> ")
        if userInput == "fight":
            if weapon:
                print("\nYou slay the vile beast and continue on to the next room. Congratulations on your conquest!\n")
            empty11()
        else:
            print("\nYou are slain by the vile beast and rot there for eternity.\n\n")
            print("GAME OVER")
            quit()
   
#code for empty11 room
def empty11():
    directions = ["right","back"]
    print("\nYou've made it into a small room that appears to be empty. The walls are made of large stone. The floor is")
    print("damp and there is a trickling sound in the distant.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: right/back\n")
        userInput = input("> ")
        if userInput == "right":
            monster13()
        elif userInput == "back":
            cavernStart()
        else:
            print("Please enter a valid option")
            
#code for monster13 room
def monster13():
    actions = ["fight","flee"]
    print("\nAs you enter the next chamber, you hear a heavy breathing sound. The creature making this sounds enormous.")
    print("The hair on your arms stands up and you feel the fight/flight response surging inside your body.\n")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee\n")
        userInput = input("> ")
        if userInput == "fight":
            print("\nYour sword starts to glow brighter and brighter as the breathing gets louder. You can feel your heart")
            print("pounding and your senses becoming acutly aware of everything around you. The creature reveals itself and")
            print("rushes toward you. It's an 8 foot tall werewolf with arms as long as you. He has claws that are several")
            print("inches long and hair that is stained with blood. He takes a swipe at you, and you swing your sword,")
            print("striking his arm. Smoke eminates from where you struck him and he lets out a blood curdling howl in pain.")
            print("His howl transforms into a scream, like that from a human. He transfigures into a man, laying in a ball")
            print("on the ground crying. You approach him and ask him who he is. He looks up at you with tears in his eyes")
            print("and says, my name is Tom Heffron and I\'m sorry for attacking you. I can\'t control myself when I\'m like")
            print("that. He looks at you and your sword which is not glowing anymore and says, \"That is The Sword of Trans-")
            print("wolftation. He goes on to tell you that striking him with that sword while in werewolf form removes the")
            print("curse and returns him to human form, permanently\n")
            print("You ask him what is beyond this room in the catacombs, but he's in too much pain to answer.\n")
            level1End()
        elif userInput == "flee":
            print("You leave the cave and return home a coward. You die alone and nobody likes you.")
            print("GAME OVER")
            quit()
        else:
            print("Please enter a valid option")

#code for empty12 room
def empty12():
    directions = ["forward","back"]
    print("\nYou've made it into a small room that appears to be empty. The walls are made of large stone")
    print("The floor is damp and there is a trickling sound in the distant\n")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/back\n")
        userInput = input("> ")
        if userInput == "forward":
            dead11()
        elif userInput == "back":
            cavernStart()
        else:
            print("Please enter a valid option")

#code for dead11 room
def dead11():
    print("\nAs you enter the dimly lit room, the floor gives way and you fall through it, plumeting to your death.\n")
    print("GAME OVER")
    quit()

#code for level1End room
def level1End():
    directions = ["descend","right"]
    print("\nYou continue down a corridor and enter a room with glowing orbes on the wall. At the far wall is a ladder.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: descend/right/back\n")
        userInput = input("> ")
        if userInput == "descend":
            level2Start()
        elif userInput == "right":
            dead21()
        elif userInput == "back":
            level1End()
        else:
            print("Please enter a valid option")

#code for level2Start
def level2Start():
    directions = ["forward","right"]
    print("\nAt the top of the ladder, you enter a cavern 20 feet wide by 50 feet long. To your right is a small opening, and")
    print("in front of you is another long corridor.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/right\n")
        userInput = input("> ")
        if userInput == "forward":
            empty21()
        elif userInput == "right":
            dead21()
        else:
            print("Please enter a valid option")

#code for dead21 room
def dead21():
    print("\nYou trip, hit your head, pass out and awaken to being eaten alive by ants. So sad.\n")
    print("GAME OVER")
    quit()

#code for empty21 room
def empty21():
    directions = ["right","back"]
    print("\nAs you enter this room, you hear a strange noise off in the distance. The room is dimly lit and there are claw.\n")
    print("marks on the wall. You see a pool of blood on the floor in front of an opening to your right.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: right/back\n")
        userInput = input("> ")
        if userInput == "right":
            monster21()
        elif userInput == "back":
            level2Start()
        else:
            print("Please enter a valid option")
            
#code for monster21 room
def monster21():
    actions = ["fight","flee"]
    global weapon
    print("As you enter the opening, you draw your sword. This time is pulsates red and vibrates in your hand. It's as if it's")
    print("trying to tell you to beware.\n")
    print("Just as you look down at your sword, a Demigorgon jumps out of the shadows and lets out a sound so loud, your ears")
    print("are ringing.\n")
    userInput = ""
    while userInput not in actions:
        print ("Options: flee/fight\n")
        userInput = input("> ")
        if userInput == "fight":
            print("\nThe Demigorgon lunges at you and catches one of it's teeth on your jacket. It's a good thing it didn't pierce")
            print("your skin, as it carries a venom that turns you into a goon. You swing at it, taking it's head clean off, but")
            print("breaking your sword in the process. The beast is no more.\n")
            weapon = False
            gold21()
        elif userInput == "flee":
            print("\nYou are slain by the vile beast as you turn to get away. He has turned you into a schmoo.\n")
            print("GAME OVER")
            quit()
        else:
            print("Please enter a valid option")

#code for gold21 room
def gold21():
    directions = ["right","back"]
    print("\nYou press on into another chamber and as you walk in, you see a golden coin by your feet. Off in the distance, you")
    print("can see something else shimmering by the next corridor. You can't help but think that somehting is leading you")
    print("onward.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: right/back\n")
        userInput = input("> ")
        if userInput == "right":
            sword21()
        elif userInput == "back":
            monster21()
        else:
            print("Please enter a valid option")
            
#code for sword21 room
def sword21():
    directions = ["forward","left","back"]
    global weapon
    print("\nYou're walking down a hallway and trip on something. You reach down to pick it up and it's a katana sword\n")
    weapon = True
    userInput = ""
    while userInput not in directions:
        print("Options: forward/left/back\n")
        userInput = input("> ")
        if userInput == "forward":
            monster22()
        elif userInput =="left":
            level3Start()
        elif userInput == "back":
            gold21()
        else:
            print("Please enter a valid option")
            
#code for monster22 room
def monster22():
    actions = ["fight","flee"]
    global weapon
    print("You can hear something that sounds like moaning in the distance...but it's drawing closer.")
    userInput = ""
    while userInput not in actions:
        print ("Options: flee/fight\n")
        userInput = input("> ")
        if userInput == "fight":
            if weapon:
                print("\nYou draw your katana and out of the shadows emerges a creeper. Not just any creeper, but Terry_Kreeper\n")
                print("The zombie lunges at you, but it is very slow. You slice at it's legs and cut them clean off. The")
                print("creeper lays there wiggling around and is no longer a threat. Good job at slaying Terry_Kreeper!\n")
                gold21()
            else:
                print("Out of the shadows emerges a creeper. It lunges at you and eats your brains. It was only a meer snack\n")
                quit()
        elif userInput == "flee":
            print("\nYou run home crying to mommy and never go on any adventures again.\n")
            print("GAME OVER")
            quit()
        else:
            print("Please enter a valid option")

#code for gold22 room
def gold22():
    directions = ["left","back"]
    print("\nYou press on into the next chamber and as you walk in, you see a golden coin by your feet. Off in the distance,")
    print("you can see something else shimmering by the entrance to the next area. You still can't shake that feeling that")
    print("somehting is leading you onward.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: left/back\n")
        userInput = input("> ")
        if userInput == "left":
            level2End()
        elif userInput == "back":
            monster22()
        else:
            print("Please enter a valid option")

#code for level3Start room
def level2End():
    directions = ["descend","back"]
    print("\nYou emerge into a large room and another ladder is in the middle.\n")
    userInput = ""
    while userInput not in directions:
        print("Options: descend/back\n")
        userInput = input("> ")
        if userInput == "descend":
            level3Start()
        elif userInput == "back":
            monster22()
        else:
            print("Please enter a valid option")

def level3Start():
    global weapon
    if weapon:
        print("\nAs you make your way down the ladder, you enter a large chamber filled with more gold and jewels than you could")
        print("ever imagine. You see a cave to the right and movement in it. You draw your sword and cry out, \"Bring your")
        print("worst vile demon. Balrog, the giant beast that was driven out of Moria appears from the shadows and lets out a")
        print("battle cry that sends shivers up your spine. You swing from a rope and land on it's back. What happens next,")
        print("you'll have to wait and see.\n\n")
        print("To be continued...")
        quit()

print("\n\nWelcome to an adventure created for Alexander and Madeline!\n")
print("During this adventure, you can use simple commands like \"left\", \"right\", \"backwards\", and \"forwards\", to")
print("navigate around\n")
print("Let's start with your name:\n")
name = input("Name: ")
print("\nGoodluck on your adventure, " + name + ".\n\n")
print("You are exploring around the lookout at Kalamalka Lake and come across an old abandoned shack imbedded into the side")
print("of the mountain. You've heard stories about an old hermit named Tom Heffron and wonder if this might have been where")
print("he lived. You pry off the weathered boards covering the entrance and enter the shack and see a table and chair, some")
print("newspapers on the floor in the shape of a bed, and what looks like a bookshelf against the wall. Standing in front")
print("of the bookshelf, you notice a couple old books about geology, minine, and identifying gold. As you stand there")
print("looking at the books, you feel a cold breeze coming from cracks in the shelf.\n")
cavernStart()
