'''
Below is the pattern we will use to create the story.
###############################################################################
Theme = mystery, adventure, exploration
Setting (house, The Expanse, etc.)
    Goal (fetch this, go here)
        Goal (fetch this, go here)
            Goal (fetch this, go here)
            method (don't kill, use bows, trade for, etc)
            complication (work only during night, use training weapons, Dire monsters, bad clues,  etc)
        method (don't kill, use bows, trade for, etc)
        complication (work only during night, use training weapons, Dire monsters, bad clues,  etc)
    method (don't kill, use bows, trade for, etc)
    complication (work only during night, use training weapons, Dire monsters, bad clues,  etc)
'''

import random
themes = ['mystery', 'adventure', 'exploration']
settings = ['The Expanse', 'Tyshau', 'your house', 'Neo-Lilar']
goals = {'mystery': ['fetch', 'go to'],
         'adventure': ['fetch', 'go to', 'destroy'],
         'exploration': ['fetch', 'go to', 'build']}
methods = ['don\'t kill', 'trade for', 'use musical instrument']
complications = ['work only during night', 'monsters', 'bad clues']

class story():
    global theme
    theme = random.choice(themes)

    global setting
    setting = random.choice(settings)
    settings.remove(setting)

    goal = random.choice(goals[theme])
    if goal == 'fetch':
        global item
        item = random.choice(['medicine', 'food', 'gold'])
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
Theme: {theme}.
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
    -Method: {self.method}
    -Complication: {self.complication}
    -Reward: {self.reward}"""
        return self.substory

story = story()
print(story)
substory = substory()
#print(story,substory)