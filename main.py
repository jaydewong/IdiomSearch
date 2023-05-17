"""
import idiomatch

main

terminal text input

idiomatch search and return output
"""

import sys
import spacy
import threading
from idiomatch import Idiomatcher
from build_database import build
from build_database import search
from build_idiomatcher import buildIdiomatcher
from build_idiomatcher import matchIdiom

run_setup = False

#Setup Idiomatcher and Pandas Idiom Database 
def setup():
    global run_setup
    global nlp
    global idiomatcher

    t1 = threading.Thread(target=setupIdiomatcher)
    t2 = threading.Thread(target=setupDatabase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Setup Complete")
    run_setup = True

def setupIdiomatcher():
    global nlp 
    global idiomatcher 
    
    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher= Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.
    print("Idiomatcher complete")

def setupDatabase():
    build(); 

#Search Pandas database 
def searchDatabase(query):
    search(query)

def is_idiom(input):

    doc = nlp(input) # process the sentence with an nlp pipeline

    return str(idiomatcher.identify(doc))


def main():
    if (not run_setup):
        setup()

    test = input("test input (enter 'stop' to exit): ")
    while (test != "stop"):
        processed = nlp(test)
        print(idiomatcher.identify(processed))
        test = input("test input (enter 'stop' to exit): ")

    print("Program stopped. "); 

if __name__ == '__main__':
    setup()
    main()
