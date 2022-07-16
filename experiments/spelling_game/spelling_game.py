from nltk.corpus import words
word_list = words.words()
# prints 236736

running = True
final_word = ""
while running is True:
    str = input("Enter a letter: ")
    if len(str) > 1:
        str = "" 
        print("Please enter only one letter.")
    else:
        final_word = final_word + str  
        print("You:", final_word)
        possible_word = [word for word in word_list if word[0:len(final_word)] == final_word]
        if len(possible_word) == 0:
            print(f"""That's no way to spell a word!
Final word length: {len(final_word)}""")
            running = False
        elif len(possible_word) == 1:
            print(f"Ah, the word is {possible_word}, right?")
            running = False
