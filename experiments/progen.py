'''
Below is the pattern we will use to create the story.
###############################################################################
Theme = mystery, adventure, exploration
Setting (house, The Expanse, etc.)
    Goal (fetch this, go here)
        Goal (fetch this, go here)
            Goal (fetch this, go here)
            method (don't kill, use bows, trade for, etc)
            complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
        method (don't kill, use bows, trade for, etc)
        complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
    method (don't kill, use bows, trade for, etc)
    complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
'''

import random, names

themes = ['mystery', 'adventure', 'exploration']
settings = ['The Expanse', 'Tyshau', 'your house', 'Neo-Lilar']
goals = {'mystery': ['fetch', 'go to'],
         'adventure': ['fetch', 'go to', 'destroy'],
         'exploration': ['fetch', 'go to', 'build']}
methods = ['don\'t kill', 'trade for', 'use musical instrument']
complications = ['you\'ll work only during the night', 'monsters', 'bad clues']

class character(object):
    def __init__(self) -> None:
        self.gender = random.choice(["male", "female"])
        self.name = names.get_full_name(gender=self.gender)

    def __str__(self) -> str:
        return self.name +" ("+ self.gender + ")"


class story(object):
    global theme
    theme = random.choice(themes)

    global setting
    setting = random.choice(settings)
    settings.remove(setting)

    goal = random.choice(goals[theme])
    if goal == 'fetch':
        global item
        item = random.choice(['medicine', 'food', 'gold']) #main item to get
        goal = 'fetch ' + item
    elif goal == 'go to':
        goal = 'go to ' + random.choice(settings)
    elif goal == 'destroy':
        creatures = ['dragon', 'monster']
        things = ['ring', 'sheet music']
        
        item = random.choice([random.choice(creatures), random.choice(things)])
        goal = 'destroy ' + item

    method = random.choice(methods)
    if method == 'trade for':
        try:
            method ='trade for ' + item
        except NameError:
            method = 'trade for ' + random.choice(['medicine', 'food', 'gold'])
    elif method == 'use musical instrument':
        global instrument
        instruments = ['piano', 'guitar', 'drum', 'violin']
        instrument = random.choice(instruments)
        method = 'use ' + instrument

    complication = random.choice(complications)

    def __str__(self):
        story = f"""-----------------------------------------------------
Theme: {theme}
Setting: {setting}
Main Goal: {self.goal}
    -Method: {self.method},
    -Complication: {self.complication}
-Subgoal 1: {substory()}
-Subgoal 2: {substory()}
-Subgoal 3: {substory()}
-----------------------------------------------------"""
        return story

class substory(object): 
    setting = setting
    theme = theme

    def __init__(self) -> None:
        self.goal = random.choice(goals[theme])
        if self.goal == 'fetch':
            global item
            item = random.choice(['medicine', 'food', 'gold'])
            self.goal = 'fetch ' + item
        elif self.goal == 'go to':
            self.goal = 'go to ' + random.choice(settings)
        elif self.goal == 'destroy':
            creatures = ['a dragon', 'some monster']
            things = ['a ring', 'sheet music']
            
            item = random.choice([random.choice(creatures), random.choice(things)])
            self.goal = 'destroy ' + item

        self.method= random.choice(methods)
        if self.method== 'trade for':
            try:
                self.method='trade for ' + item
            except NameError:
                self.method= 'trade for ' + random.choice(['medicine', 'food', 'gold'])
        elif self.method== 'use musical instrument':
            global instrument
            instruments = ['piano', 'guitar', 'drum', 'violin']
            instrument = random.choice(instruments)
            self.method= 'use ' + instrument #player should be given an instrument at this point

        self.complication = random.choice(complications)
        
        try:
            self.reward = random.choice(['medicine', 'food', 'gold', instrument])
        except NameError:
            self.reward = random.choice(['medicine', 'food', 'gold'])

    def __str__(self):
        self.substory = f"""
    -Goal: {self.goal}
    -Proposed by: {character()}
    -Method: {self.method}
    -Complication: {self.complication}
    -Reward: {self.reward}"""
        return self.substory
    
    def tell(self):
        self.substory = f"""
Hey, I'm {character()} and I'm here to help you.
I just need to {self.goal}.
Of course it'll be hard because...{self.complication}.
But, uh, I'll give you that {self.reward} you need."""
        print(self.substory)

story = story()
#print(story)
substory = substory()
substory.tell()