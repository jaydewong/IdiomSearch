"""
import idiomatch

main

terminal text input

idiomatch search and return output
"""

import json
import sys
import spacy
import threading
from idiomatch import Idiomatcher
from build_database import buildDatabase
from build_database import searchDatabase
from build_idiomatcher import buildIdiomatcher
from build_idiomatcher import matchIdiom 

run_setup = False

#Setup Idiomatcher and Pandas Idiom Database 
def setup():
    global run_setup
    global nlp
    global idiomatcher

    t1 = threading.Thread(target=buildIdiomatcher)
    t2 = threading.Thread(target=buildDatabase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Setup Complete")
    run_setup = True

#Match the idiom to the given input from JS file
def searchInputInDatabase(input):

    #get and parse an Idiomatcher match if it exists 
    idiomList = matchIdiom(input)
    print("The list of idioms is: " + idiomList)
    
    #search idiomList in Pandas database - currently returns part of speech
    print("Printing examples of matched idioms...")
    result = searchDatabase(idiomList)
    return result

#Testing functions with console input 
def main():
    global nlp 

    if (not run_setup):
        setup()

    test = input("test input (enter 'stop' to exit): ")
    while (test != "stop"):
        #print(matchIdiom(test))
        print(searchInputInDatabase(test))
        #print(idiomatcher.identify(processed))
        #searchInputInDatabase(idiomatcher.identify(processed))

        test = input("test input (enter 'stop' to exit): ")

    print("Program stopped. "); 

if __name__ == '__main__':
    setup()
    main() 
