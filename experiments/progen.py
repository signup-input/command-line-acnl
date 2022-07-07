'''
Below is the pattern we will use to create the story.
###############################################################################
Theme = mystery, adventure, exploration
Setting (house, The Expanse, etc.)
    Goal (fetch this, go here)
        Goal (fetch this, go here)
            Goal (fetch this, go here)
            method (don't kill, use bows, trade for, bad clues,  etc)
            complication (only during night, use training weapons, Dire monsters, bad clues,  etc)
        method (don't kill, use bows, trade for, bad clues,  etc)
        complication (only during night, use training weapons, Dire monsters, bad clues,  etc)
    method (don't kill, use bows, trade for, bad clues,  etc)
    complication (only during night, use training weapons, Dire monsters, bad clues,  etc)
'''

import random
themes = ['mystery', 'adventure', 'exploration']
settings = ['The Expanse', 'Tyshau', 'your house', 'Neo-Lilar']
goals = {'mystery': ['fetch', 'go to'],
         'adventure': ['fetch', 'go to', 'destroy'],
         'exploration': ['fetch', 'go to', 'build']}
methods = ['don\'t kill', 'trade for', 'bad clues']
complications = ['only during night', 'monsters', 'bad clues']

class story():
    theme = random.choice(themes)
    setting = random.choice(settings)
    goal = random.choice(goals[theme])
    if goal == 'fetch':
        object = random.choice(['medicine', 'food', 'gold'])
    method = random.choice(methods)
    if method == 'trade for':
        method == 'trade for' + object
    complication = random.choice(complications)
    def __str__(self):
        return 'Theme: ' + self.theme + '\nSetting: ' + self.setting + '\nGoal: ' + self.goal + '\nMethod: ' + self.method + '\nComplication: ' + self.complication
    def test_story(self):
        print("-----------------------------------------------------")
        print(self.theme)
        print(self.setting)
        print(self.goal)
        print(self.method)
        print(self.complication)

story = story()
print(story)
story.test_story()