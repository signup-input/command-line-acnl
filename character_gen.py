import random, names

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
        self.motives = "get back home after being stuck in The Expanse" #!todo: randomize
        return self.motives





#print(character())