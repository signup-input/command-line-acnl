import random, names

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
narrative = ["realistic", "insane", "humorous"]#['you\'ll work only during the night', 'monsters', 'bad clues']

#motives = ["surviving", "winning", "esca"]
all_motives = '''{"Plotting": "revenge",
"Surviving": "a disaster",
"Winning": "a contest",
"Escaping": "capture",
"Pursuing": "a goal",
"Finding": ["something","someone"],
"Keeping": "secret",
"Saving": ["world","town","community","loved one","themself"],
"Building": "a better world",
"Bringing down": ["company", "government"],
"Stopping": ["something","someone from doing something"],
"Repaying": "debt"}'''

class character(object):
    def __init__(self) -> None:
        self.gender = random.choice(["male", "female"])
        self.firstname = names.get_first_name(gender=self.gender)
        self.lastmame = names.get_last_name()
        #self.motives = random.choice(list(all_motives.values()))
        
    def __str__(self) -> str:
        #if isinstance(self.motives, list):
        #    return str(random.choice(self.motives))
        #else:
        #    return str(self.motives)
        return f'''{self.firstname} {self.lastmame} ({self.gender})'''#self.name + " ("+ self.gender + ")"

class story(object):
    genre = random.choice(genres)
    setting = random.choice(settings)
    settings.remove(setting)
    goal = random.choice(goals[genre])
    dep='''if goal == 'fetch':
        item = random.choice(['medicine', 'food', 'gold'])
        goal = goal + ' ' + item
    elif goal == 'go to':
        quest = random.choice(settings)
        goal = goal + ' ' + quest
    elif goal == 'destroy':
        creatures = ['dragon', 'monster']
        things = ['ring', 'sheet music']
        
        item = random.choice([random.choice(creatures), random.choice(things)])
        goal = 'destroy ' + item
    elif goal == 'build':
        buildables = ['a house', 'a tower', 'a castle', 'a better world']
        buildable = random.choice(buildables)
        if buildable == 'a better world':
            goal = 'build a better world (flesh this out)'
        else:
            goal = 'build ' + buildable'''

    narrative = random.choice(narrative)

    def __str__(self):
        story = f"""-----------------------------------------------------
Genre: {self.genre.capitalize()}
Setting: {self.setting}
Narrative: {self.narrative}
-----------------------------------------------------"""
        return story

story = story()
print(story)
#print(character())