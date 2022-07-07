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
        method = 'use ' + random.choice(['piano', 'guitar', 'drums', 'violin'])

    complication = random.choice(complications)
    
    def __str__(self):
        return "-----------------------------------------------------\nTheme: " + theme + "\nSetting: " + setting + "\n-Goal: " + self.goal + "\n-Method: " + self.method + "\n-Complication: " + self.complication + "\n-----------------------------------------------------\n"
    

class substory():
    setting = setting
    theme = theme
    goal = random.choice(goals[theme])
    if goal == 'fetch':
        global item
        item = random.choice(['medicine', 'food', 'gold'])
        goal = 'fetch ' + item
    elif goal == 'go to':
        goal = 'go to ' + random.choice(settings)
    method = random.choice(methods)
    if method == 'trade for':
        try:
            method ='trade for ' + item
        except NameError:
            method = 'trade for ' + random.choice(['medicine', 'food', 'gold'])
    elif method == 'use musical instrument':
        method = 'use ' + random.choice(['piano', 'guitar', 'drums', 'violin']) #player should be given an instrument at this point
    complication = random.choice(complications)

    def __str__(self):
        self.substory = f"""-----------------------------------------------------
        'Tis a story of great {self.theme}.
        You're in {self.setting}
        and must {self.goal}
        By the way: ({self.method},
        {self.complication})
        -----------------------------------------------------"""
        return self.substory

story = story()
print(story)
substory = substory()
#print(story,substory)