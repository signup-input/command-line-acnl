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
            return ["he","him", "his"]
        elif self.gender == "female":
            return ["she","her","hers"]

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