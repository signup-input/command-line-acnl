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
narrative = ["realistic", "insane", "humorous"]


class character(object):
    def __init__(self) -> None:
        self.gender = random.choice(["male", "female"])
        self.firstname = names.get_first_name(gender=self.gender)
        self.lastname = names.get_last_name()
        
    def __str__(self) -> str:
        return f'''{self.firstname} {self.lastname} ({self.gender})'''
    
    def firstname(self):
        return self.firstname
    
    def lastname(self):
        return self.lastname

    def gender(self):
        return self.gender
    
    def pronouns(self):
        if self.gender == "male":
            return ["he","him", "his","brother"]
        elif self.gender == "female":
            return ["she","her","hers","sister"]

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
        {random.choice(["best friend",sc.pronouns()[3]])}
        story = f'''----------------------\n"{sc.firstname}" I call. "Wait up!"
{sc.pronouns()[0].capitalize()} is far ahead of me, {random.choice(["weaving through a crowd", "sprinting", "ramming into people like a maniac"])}.
"Don't let me lose {sc.pronouns()[1]}." I think aloud.
"{sc.firstname}!" I call again. 
I have lost {sc.pronouns()[1]} completely.
"{random.choice(["No! Great.",'Come back.',"I'm sorry!", f"We have to go together! {sc.firstname}..."])}" I {random.choice(["groan","shout into the air", "whisper"])} as people continue to move around me.
I make it to {random.choice(["""another platform and lean on the guardrail.
I look down at the track below""", "a metal bench and throw myself on it", 'a large clock. "How grim." I realize'])}, {random.choice(['sighing', 'sobbing', 'scrubbing my tears away', 'willing myself not to cry. Tough people dont cry...'])}.
My train is gone and I have no way to buy another ticket.
On top of that, I've lost {random.choice([f"{sc.firstname}, my {random.choice(["best friend",sc.pronouns()[3]])}","the only person I know"])}.
Am I going to get {random.choice(["home", "back", "to Enchante"])}?
If so, how?\n-----------------------------------------------------'''
        return story

story = story()
scroll(str(story))
#print(character())