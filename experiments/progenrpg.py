'''
Below is the pattern we will use to create the story.
###############################################################################
Theme = mystery, adventure, exploration
Setting (house, The Expanse, etc.)
    Goal (fetch this, go here)
        Goal (fetch this, go here)
            Goal (fetch this, go here)
            rule (don't kill, use bows, trade for, etc)
            complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
        rule (don't kill, use bows, trade for, etc)
        complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
    rule (don't kill, use bows, trade for, etc)
    complication (you\'ll work only during the night, use training weapons, Dire monsters, bad clues,  etc)
'''

import random, names

themes = ['mystery', 'adventure', 'exploration']
settings = ['The Expanse', 'Tyshau', 'your house', 'Neo-Lilar']
goals = {'mystery': ['fetch', 'go to'],
         'adventure': ['fetch', 'go to', 'destroy'],
         'exploration': ['fetch', 'go to', 'build']}
rules = ['don\'t kill', 'trade for', 'use musical instrument']
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
        main_quest_setting = random.choice(settings)
        if main_quest_setting == 'your house':
            goal = 'go to your house (Why-ever you\'re not there.)'
    elif goal == 'destroy':
        creatures = ['dragon', 'monster']
        things = ['ring', 'sheet music']
        
        item = random.choice([random.choice(creatures), random.choice(things)])
        goal = 'destroy ' + item

    rule = random.choice(rules)
    if rule == 'trade for':
        try:
            rule ='trade for ' + item
        except NameError:
            item = random.choice(['medicine', 'food', 'gold'])
            rule = 'trade for ' + item
        if item == 'medicine':
            rule = '''trade for medicine 
            (Maybe a friend of yours is sick or you are...or some other rpg kinda thing.
            Flesh out the rest of the story)'''
        elif item == 'gold':
            rule = 'gold (Why do you need money? Flesh out.)'

    elif rule == 'use musical instrument':
        global instrument
        instruments = ['piano', 'guitar', 'drum', 'violin']
        instrument = random.choice(instruments)
        rule = 'use ' + instrument + ''' 
        (You\'ll have to memorize some sort of oot style music sequences.
        They may open doors or help you fight. Flesh out.)'''
    elif rule == 'don\'t kill':
        rule = 'don\'t kill (There are monsters. Flesh out.)'


    complication = random.choice(complications)
    if complication == 'you\'ll work only during the night':
        complication = 'you\'ll work only during the night (You may need to sneak. Flesh out.)'
    elif complication == 'monsters':
        complication = 'monsters (You may need to fight or avoid. You could die. Flesh out.)'

    def __str__(self):
        story = f"""-----------------------------------------------------
Theme: {theme}
Setting: {setting}
Main Goal: {self.goal}
    -Rule: {self.rule},
    -Complication: {self.complication}
#-Subgoal 1: {substory()}
#-Subgoal 2: {substory()}
#-Subgoal 3: {substory()}
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
            quest_setting = random.choice(settings)
            if quest_setting == "The Expanse":
                quest_setting = "The Expanse (flesh this out)"
                self.goal = 'go to ' + quest_setting
            elif quest_setting == "Tyshau":
                quest_setting = "Tyshau (flesh this out)"
                self.goal = 'go to ' + quest_setting
            elif quest_setting == "your house":
                quest_setting = "your house (flesh this out)"
                self.goal = 'go to ' + quest_setting
            elif quest_setting == "Neo-Lilar":
                quest_setting = "Neo-Lilar (flesh this out)"
                self.goal = 'go to ' + quest_setting
            else:
                self.goal = 'go to ' + quest_setting
        elif self.goal == 'destroy':
            creatures = ['a dragon', 'some monster']
            things = ['a ring', 'sheet music']
            
            item = random.choice([random.choice(creatures), random.choice(things)])
            self.goal = 'destroy ' + item
        elif self.goal == 'build':
            buildables = ['a house', 'a tower', 'a castle', 'a better world']
            buildable = random.choice(buildables)
            if buildable == 'a better world':
                self.goal = 'build a better world (flesh this out)'
            else:
                self.goal = 'build ' + buildable

        self.rule= random.choice(rules)
        if self.rule== 'trade for':
            try:
                self.rule='trade for ' + item
            except NameError:
                self.rule= 'trade for ' + random.choice(['medicine', 'food', 'gold'])
        elif self.rule== 'use musical instrument':
            global instrument
            instruments = ['piano', 'guitar', 'drum', 'violin']
            instrument = random.choice(instruments)
            self.rule= 'use ' + instrument #player should be given an instrument at this point

        self.complication = random.choice(complications)
        
        try:
            self.reward = random.choice(['medicine', 'food', 'gold', instrument])
        except NameError:
            self.reward = random.choice(['medicine', 'food', 'gold'])

    def __str__(self):
        self.substory = f"""
    -Goal: {self.goal}
    -Proposed by: {character()}
    -Rule: {self.rule}
    -Complication: {self.complication}
    -Reward: {self.reward}"""
        return self.substory
    
    def tell(self):
        self.substory = f"""Hope you like it here in {setting}.
Hey, I'm {character()} and I'm here to help you.
I just need to {self.goal}.
Of course it'll be hard because...{self.complication}.
But, uh, I'll give you that {self.reward} you need."""
        print(self.substory)

story = story()
print(story)
substory = substory()
#substory.tell()