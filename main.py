import random, sys, time, json, datetime, unittest
from text_scroll_module import scroll
from character_gen import character #!todo add to tests

title = "Animal Crossing"
ver = "v1.0.0"

cmd_fmt = "==={}===\nYou: "
cmd_fmt2 = "|{}|\nYou: "

fruits = ["apple", "banana", "orange", "pear", "strawberry"]
furniture = ["chair", "table", "bed", "desk", "couch"]

manual = {
    "outdoors": '''===Manual===
Actions:
-Got to store
-Pick flowers
-Shake a tree
-Talk to someone
-Visit someone
-View passport
-Go home
-Go to work
-Save and quit''',
    "store": '''===Manual===
Actions:
--buy
--sell
--leave''',
    "passport": '''===Manual===
Actions:
-edit
--name
--phrase
-put passport away''',
}



def help():
    helped = False
    while helped == False:
        scroll(
            f"===You are (in the/at the/viewing your) {setting}.===\n===Want some help? (y/n)==="
        )
        help_prompt = input("You: ")
        if help_prompt == "y":
            scroll(manual[setting])
            helped = True
        elif help_prompt == "n":
            scroll("'K then.")
            helped = True
        else:
            helped = False

def load():#!todo add to tests
    try:
        f = open("save_data/dat.json", "r")
        save_data = json.loads(f.read())
        f.close()
        #all variables are now loaded from the save file
        global username, pockets, phrase, town_fruit, residents
        username = save_data["name"]
        pockets = save_data["pockets"]
        phrase = save_data["phrase"]
        town_fruit = save_data["town_fruit"]
        residents = save_data["residents"]
        print(f"Loaded {username}'s data.")
        return True
    except:
        return False

def save(): #!todo add to tests
    scroll("Saving data...")

    dictionary ={
        "name" : username,
        "phrase" : phrase,
        "pockets" : pockets,
        "town_fruit" : town_fruit,
        "residents" : residents,
    }
    
    with open("save_data/dat.json", "w") as outfile:
        json.dump(dictionary, outfile)
    print(f"Saved {username}'s data.")

#Start of game
load = load()
if load == True:
    scroll(f"Welcome back to {title}, {ver}!")
    scroll(f"You're the one they call {username}, right?")
elif load == False:
    scroll(f"Welcome to {title}, {ver}!")
    username = input(cmd_fmt.format("What should we call you?"))
    phrase = input(cmd_fmt.format("Tell us your catchphrase."))
    town_fruit = random.choice(fruits)

    dictionary ={
        "name" : username,
        "phrase" : phrase,
        "pockets" : [],
        "town_fruit" : town_fruit,
        "residents" : [character().firstname, character().firstname, character().firstname],
    }
    
    with open("save_data/dat.json", "w") as outfile:
        json.dump(dictionary, outfile)

    scroll(f'You: I\'m, {username}. \"{phrase.capitalize()}\".')
    scroll(f"Well, \"{phrase}\" to you too, {username}.")
    
print("===========================================================")
print("===========================================================")

passport = f'''===Passport===
Name: {username}
Catchphrase: {phrase}
Date of Birth: ###/###/####'''

#game loop
running = True
while running == True:
    cmd = input(cmd_fmt.format("What would you like to do?")).lower()
    setting = "outdoors"

    #you can't save or view manual at any time, only in this part of the loop
    if cmd == "see manual" or cmd == "manual":
        scroll(manual["setting"])
    elif cmd == "save and quit":
        save()
        scroll("See you soon!")
        running = False

    elif cmd == "go to the store":
        setting = "store"

        scroll("You go to the store.")
        while setting == "store":
            store_cmd = input(cmd_fmt.format("What would you like to do here?"))
            if store_cmd == "sell":
                scroll("Feature not yet implemented.")
            elif store_cmd == "buy":
                scroll("You ask the shopkeeper what is for sale.")
                scroll("Feature not yet implemented.")

            elif store_cmd == "leave":
                setting = "outdoors"

            else:
                help()

    elif cmd == "pick flowers":
        scroll("You begin to pick flowers.")
        input("Press Enter to pick a flower.")
        scroll("Feature not yet implemented.")
    elif cmd == "shake a tree":
        scroll("Feature not yet implemented.")
        scroll("You start to shake a tree.")
        items = [
            f"{town_fruit}", f"{random.choice(furniture)}", "stick"
        ]
        for i in range(random.randint(1, 9)):
            input("Press Enter to shake the tree.")
            if random.randint(1, 3) == 3:
                scroll(f"You got one: {random.choice(items).strip()}")
            
            else:
                scroll("Nothing happened.")
        scroll("Your arms got tired")

    elif cmd == "talk to someone":
        #scroll(f"You approach {}.")
        scroll("You approach a person. They ask if you would like to play a game.")
        scroll("(You don't have a choice yet.)")
        scroll("You play a game with them.")
        import spelling_game #!todo add to tests
        pass
    elif cmd == "visit someone":
        #scroll(f"You visit {}.")
        scroll("You visit a person.")
        scroll("Feature has not been implemented yet.")
        scroll("You leave.")
        pass

    elif cmd == "view passport":
        setting = "passport"

        scroll(f"You view your passport.")
        scroll(passport)
        viewing = True
        while viewing == True:
            passport_cmd = input(cmd_fmt.format("What now?"))
            if passport_cmd == "edit":
                edit_cmd = input(cmd_fmt.format("Change what?"))
                if edit_cmd == "name":
                    new_name = input(cmd_fmt.format("What should we call you?"))
                    scroll(f"You change your name to {new_name}.")
                    username = new_name
                    save()
                elif edit_cmd == "phrase":
                    new_phrase = input(cmd_fmt.format("What should we change it to?"))
                    scroll(f"You change your phrase to {new_phrase}.")
                    phrase = new_phrase
                    save()
                else:
                    scroll("You can't change that.")
                #pass
            elif passport_cmd == "put passport away":
                viewing = False
            else:
                help()
        
        scroll("You put away your passport.")

    elif cmd == "go home":
        scroll("You go home.")
        scroll("Feature has not been implemented yet.")
        pass

    elif cmd == "go to work":
        scroll("You go to work.")
        setting = "work"
        scroll("Feature has not been implemented yet.")
        pass
    
    elif cmd == "play with my pet":
        scroll("You play with your pet.")
        import pet #!todo add to tests
        
    else:
        help()


sys.exit()