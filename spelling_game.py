from text_scroll_module import scroll
from nltk.corpus import words
word_list = words.words()


running = True
final_word = ""
while running is True:
    str = input("Enter a letter: ")
    if len(str) > 1:
        if str == "quit":
            scroll("Oh, you want to stop? Okay.")
            running = False
        else:
            str = "" 
            scroll("Please enter only one letter.")
    elif len(str) == 0:
        scroll("Please enter a letter.")
    
    else:
        final_word = final_word + str  
        scroll("You: " + final_word)
        possible_word = [word for word in word_list if word[0:len(final_word)] == final_word]
        if len(possible_word) == 0:
            scroll(f"""That's no way to spell a word!
Final word length: {len(final_word)}""")
            running = False
        elif len(possible_word) == 1:
            scroll(f"Ah, the word is {possible_word}, right?")
            running = False
