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
narrative = ["realistic", "insane", "humorous"]


class character(object):
    def __init__(self) -> None:
        self.gender = random.choice(["male", "female"])
        self.firstname = names.get_first_name(gender=self.gender)
        self.lastmame = names.get_last_name()
        
    def __str__(self) -> str:
        return f'''{self.firstname} {self.lastmame} ({self.gender})'''#self.name + " ("+ self.gender + ")"

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
        return story

story = story()
print(story)
#print(character())