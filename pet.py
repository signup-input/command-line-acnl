import random,json,sys
from text_scroll_module import scroll

def load():
    try:
        f = open("pet_dat.json", "r")
        save_data = json.loads(f.read())
        f.close()
        #all variables are now loaded from the save file
        global life_span, hunger, thirst, groomed, name, happiness
        life_span = save_data["life_span"]
        hunger = save_data["hunger"]
        thirst = save_data["thirst"]
        groomed = save_data["groomed"]
        name = save_data["name"]
        happiness = save_data["happiness"]
        print(f"Loaded {name}'s data.")
        return True
    except:
        happiness = 10
        life_span = 10
        hunger = 10
        thirst = 10
        groomed = True
        name = "Pet"
        return False

def save():
    scroll("Saving data...")

    dictionary ={
        "life_span" : life_span,
        "hunger" : hunger,
        "thirst" : thirst,
        "groomed" : groomed,
        "name" : name,
        "happiness" : happiness,
    }
    
    with open("pet_dat.json", "w") as outfile:
        json.dump(dictionary, outfile)
    print(f"Saved {name}'s data.")

cmd_fmt2 = "|{}|\nYou: "

load = load()
if load == True:
    scroll("You decide to play with your pet.")
elif load == False:
    scroll("Feature not yet implemented.")
    scroll("You get a puppy")
    name = input(cmd_fmt2.format("What should you name it?"))
    scroll(f"You named you puppy: {name}.")
    happiness = 10
    life_span = 10
    hunger = 10
    thirst = 10
    groomed = True
    save()

caring_for = True
while caring_for == True:
    scroll("Feature not yet implemented.")
    caring_for = False