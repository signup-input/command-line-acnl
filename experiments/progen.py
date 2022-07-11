import random, names
#gender = "male"
#s = "At least, that's what {pronoun} told me.".format(pronoun="he" if gender == "male" else "she")

import sys, time

def scroll(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)

    input("\nPress Enter...")

genres = [#'mystery',
#'adventure',
'speculative']
settings = ['The Expanse',
#'Tyshau',
#'your house',
#'Neo-Lilar'
'train station',
'bus station',
]
goals = {'mystery': ['fetch', 'go to'],
         'adventure': ['fetch', 'go to', 'destroy'],
         'speculative': ['fetch', 'go to', 'build']}
motives = ["go to Enchante and start a bakery","get back home after being stuck in The Espanse", "become the best Instrumentalist in Neo-Lilar", ]
narrative = ["realistic", "insane", "humorous"]


class character(object):
    def __init__(self) -> None:
        self.gender = random.choice(["male", "female"])
        self.firstname = names.get_first_name(gender=self.gender)
        self.lastname = names.get_last_name()
        
    def __str__(self) -> str: #returns their info as a string
        return f'''{self.firstname} {self.lastname} ({self.gender}) Wants to {self.motives()}.'''
    
    def firstname(self): #returns their first name
        return self.firstname
    
    def lastname(self): #returns their last name
        return self.lastname

    def gender(self):
        return self.gender
    
    def pronouns(self): #gives them pronouns
        if self.gender == "male":
            return ["he","him", "his","brother"]
        elif self.gender == "female":
            return ["she","her","hers","sister"]
    
    def male(self): #makes them a guy
        self.gender = "male"
        self.firstname = names.get_first_name(gender=self.gender)

    def female(self): #makes them a girl
        self.gender = "female"
        self.firstname = names.get_first_name(gender=self.gender)

    def motives(self): #gives them desires
        self.motives = "get back home after being stuck in The Expanse" #this will soon be randomized
        return self.motives



class story(object):
    genre = random.choice(genres)
    setting = random.choice(settings)
    settings.remove(setting)
    goal = random.choice(goals[genre])
    

    narrative = random.choice(narrative)

    def __str__(self):
        story = f"""-----------------------------------------------------
Genre: {self.genre.capitalize()}
Setting: {self.setting}
Narrative: {self.narrative}
-----------------------------------------------------"""
        mc = character()
        sc = character()
        mc.female() 
        sc.male() 
        print(mc)

        story = f'''Chapter One
My name is {mc.firstname} {mc.lastname}. My dream is to {mc.motives}. Me and {sc.firstname} are...
----------------------
"{sc.firstname}!" I {random.choice(["shout","scream","call"])}. "{random.choice(["Wait up!", "I said I'm sorry!", "Are you okay?", "You were serious?"])}"
{sc.pronouns()[0].capitalize()} is far ahead of me, {random.choice([f"weaving through {random.choice([f'the sea of people', 'the crowd'])}", "sprinting", "ramming into people " + random.choice(["like a maniac", f"like {sc.pronouns()[0]+' *is*'}"])])}.
"{random.choice(["Don't let me lose " + sc.pronouns()[1] + ".","How did it ever come to this?"])}" I think aloud.
"{sc.firstname}!" I call again. 
{random.choice(['I have lost ' + sc.pronouns()[1] + ' completely.', sc.pronouns()[0].capitalize() + " is gone.", sc.pronouns()[0] + " vanishes completely."])}
"{random.choice(["No! Great.",'Come back.',"I'm sorry!", f"We have to go together! {sc.firstname}..."])}" I {random.choice(["groan","shout into the air", "whisper"])} as people continue to move around me.
I {random.choice(["make it to","arrive at"])} {random.choice(["""another platform and lean on the guardrail.
I look down at the track below""", "a metal bench and throw myself on it", 'a large clock with imposing Roman numerals. "How grim." I realize'])}, {random.choice(['sighing', 'sobbing', 'scrubbing my tears away', 'willing myself not to cry. Tough people dont cry...'])}.
Our train {random.choice(["left just minutes ago","is gone"])} {random.choice(["and I have no way to buy", "There is no point in buying", "and why buy"])} another ticket.
On top of that, {random.choice(["I've lost", "I just lost"])} {random.choice([sc.firstname,"the only person " + random.choice(["I care about","in this place who cares about me","I know"])])}.
{random.choice(["Am I going to", "Am I never going to"])} {random.choice(["get", "make it"])} {random.choice(["home", "back", "to Enchante"])}?
-----------------------------------------------------'''
        return story

story = story()
scroll(str(story))
#print(character())