import random, sys, time, json

title = "Animal Crossing"
ver = "v1.0.0"

cmd_fmt = "==={}===\nYou: "
cmd_fmt2 = "|{}|"

town_fruit = "pineapple"
furniture = ["clock"]


def load():
    try:
        f = open("dat.json", "r")
        save_data = json.loads(f.read())
        #print(save_data)
        f.close()
        global username, pockets
        username = save_data["name"]
        pockets = save_data["pockets"]
        #print(f"Loaded {username}'s data.")
        return True
    except:
        #print("Error loading data.")
        return False


def scroll(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)

    input("\nPress Enter...")


load = load()
if load == True:
    scroll(
        f"Welcome back to {title}, {ver}!\nYou're the one they call {username}, right?"
    )
elif load == False:
    scroll(f"Welcome to {title}, {ver}!")
    name = input(cmd_fmt.format("What should we call you?"))
    phrase = input(cmd_fmt.format("Tell us your catchphrase."))
  
    dictionary ={
        "name" : name,
        "phrase" : phrase,
        "pockets" : []
    }
    
    with open("dat.json", "w") as outfile:
        json.dump(dictionary, outfile)

    scroll(f'You: I\'m, {name}. \"{phrase.capitalize()}\".')

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
}


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


#def whereami():
#    scroll(f"===You are in/at {setting}===\n")

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
            f"{town_fruit}", f"{random.choice(furniture)}", "stick",
            "nothing happened"
        ]
        for i in range(random.randint(1, 9)):
            input("Press Enter to shake the tree.")
            if random.randint(1, 3) == 3:
                scroll(f"You got one: {random.choice(items).strip()}")
            else:
                scroll("Nothing happened.")
        scroll("Your arms got tired")

    elif cmd == "talk to someone":
        #scroll(f"You talk to {}.")
        pass
    elif cmd == "visit someone":
        #scroll(f"You visit {}.")
        pass

    elif cmd == "view passport":
        scroll(f"You view your passport.")

    elif cmd == "go home":
        scroll("You go home.")

    elif cmd == "go to work":
        scroll("You go to work.")
        setting = "work"

    elif cmd == "save and quit":
        scroll("There is no save function as of now...")
        scroll("See you soon!")
        running = False

    else:
        help()

sys.exit()
