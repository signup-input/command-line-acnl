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

        story = f''''''
        return story

story = story()
scroll(str(story))
#print(character())