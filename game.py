import random,sys,time

def scroll(text): 
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)

    input("\nPress Enter...")

scroll("Welcome to This Game!")
manual = {"outdoors":'''===Manual===
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
"store":'''===Manual===
Actions:
--buy
--sell
--leave
-Save and quit''',}

cmd_fmt = "==={}===\nYou: "
cmd_fmt2 = "|{}|"

def help():
    helped = False
    while helped == False:        
        scroll(f"===You are (in the/at the) {setting}.===\n===Want some help? (y/n)===")
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
while running==True:
    cmd = input(cmd_fmt.format("What would you like to do?")).lower()
    setting = "outdoors"

    if cmd=="see manual":
        scroll(manual)

    elif cmd=="go to the store":
        setting ="store"

        scroll("You go to the store.")
        store_cmd = input(cmd_fmt.format("What would you like to do here?"))

        if store_cmd=="sell":
            pass
        if store_cmd=="buy":
            scroll("You ask the shopkeeper what is for sale.")

        elif store_cmd=="leave":
            pass

        else:
            help()

    elif cmd=="pick flowers":
        scroll("You begin to pick flowers.")
        input("Press Enter to pick a flower.")
    elif cmd=="shake a tree":
        scroll("You start to shake a tree.")
        input("Press Enter to shake the tree.")
        for i in range(3):
            pass
    
    elif cmd=="talk to someone":
        #scroll(f"You talk to {}.")
        pass
    elif cmd=="visit someone":
        #scroll(f"You visit {}.")
        pass
    
    elif cmd=="view passport":
        scroll(f"You view your passport.")

    elif cmd=="go home":
        scroll("You go home.")
        
    elif cmd=="go to work":
        scroll("You go to work.")
        setting = "work"
    
    elif cmd=="save and quit":
        scroll("There is no save function as of now...")
        scroll("See you soon!")
        running = False

    else:
        help()

sys.exit()