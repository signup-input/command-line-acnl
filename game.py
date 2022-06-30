import random, sys, time, json, datetime

title = "Animal Crossing"
ver = "v1.0.0"

cmd_fmt = "==={}===\nYou: "
cmd_fmt2 = "|{}|"

fruits = ["apple", "banana", "orange", "pear", "strawberry"]
furniture = ["chair", "table", "bed", "desk", "couch"]


def load():
    try:
        f = open("dat.json", "r")
        save_data = json.loads(f.read())
        #print(save_data)
        f.close()
        #all variables are now loaded from the save file
        global username, pockets, phrase, town_fruit
        username = save_data["name"]
        pockets = save_data["pockets"]
        phrase = save_data["phrase"]
        town_fruit = save_data["town_fruit"]
        #print(f"Loaded {username}'s data.")
        return True
    except:
        #print("Error loading data.")
        return False

def save():
    scroll("Saving data...")

    dictionary ={
        "name" : username,
        "phrase" : phrase,
        "pockets" : pockets,
        "town_fruit" : town_fruit,
    }
    
    with open("dat.json", "w") as outfile:
        json.dump(dictionary, outfile)
    print(f"Saved {username}'s data.")

def scroll(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)

    input("\nPress Enter...")


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
    }
    
    with open("dat.json", "w") as outfile:
        json.dump(dictionary, outfile)

    scroll(f'You: I\'m, {name}. \"{phrase.capitalize()}\".')
    #scroll("You: I'm a new player. I'm new to the game. I'm new to the town. I'm new to the world.")
    scroll(f"Well, \"{phrase}\" to you too, {name}.")
    
print("===========================================================")
print("===========================================================")


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
--leave
-Save and quit''',
    "passport": '''===Manual===
Actions:
-edit
--name
--phrase
-put passport away''',
}

passport = f'''===Passport===
Name: {username}
Catchphrase: {phrase}
Date of Birth: ###/###/####'''

def help():
    helped = False
    while helped == False:
        scroll(
            f"===You are (in the/at the) {setting}.===\n===Want some help? (y/n)==="
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

running = True
while running == True:
    cmd = input(cmd_fmt.format("What would you like to do?")).lower()
    setting = "outdoors"

    if cmd == "see manual":
        scroll(manual)

    elif cmd == "go to the store":
        setting = "store"

        scroll("You go to the store.")
        store_cmd = input(cmd_fmt.format("What would you like to do here?"))

        if store_cmd == "sell":
            pass
        if store_cmd == "buy":
            scroll("You ask the shopkeeper what is for sale.")

        elif store_cmd == "leave":
            pass

        else:
            help()

    elif cmd == "pick flowers":
        scroll("You begin to pick flowers.")
        input("Press Enter to pick a flower.")
    elif cmd == "shake a tree":
        scroll("You start to shake a tree.")
        items = [
            f"{town_fruit}", f"{random.choice(furniture)}", "stick"
        ]
        for i in range(random.randint(1, 9)):
            input("Press Enter to shake the tree.")
            if random.randint(1, 3) == 3:
                scroll(f"You got one: {random.choice(items).strip()}")
            #
            else:
                scroll("Nothing happened.")
        scroll("Your arms got tired")

    elif cmd == "talk to someone":
        #scroll(f"You approach {}.")
        scroll("You approach a person.")
        scroll("Feature has not been implemented yet.")
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
                pass
            elif passport_cmd == "put passport away":
                viewing = False
            else:
                help()
        
        scroll("You put away your passport.")

    elif cmd == "go home":
        scroll("You go home.")

    elif cmd == "go to work":
        scroll("You go to work.")
        setting = "work"

    elif cmd == "save and quit":
        save()
        scroll("See you soon!")
        running = False

    else:
        help()


sys.exit()