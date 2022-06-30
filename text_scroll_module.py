import sys, time

def scroll(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.1)

    input("\nPress Enter...")