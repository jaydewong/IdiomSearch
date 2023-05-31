"""
import idiomatch

main

terminal text input

idiomatch search and return output
"""

import json
import re
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

    print("inside setup")

    t1 = threading.Thread(target=buildIdiomatcher)
    t2 = threading.Thread(target=buildDatabase)

    print("created threads")

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
    #print("The list of idioms is: " + idiomList)
    #print(idiomList)

    if str(idiomList) == '[]':
        return "No idiom found."
    else:
         #print("Printing examples of matched idioms...")
        foundIdiom, result = searchDatabase(idiomList)

        if(foundIdiom == None):
            return "No definition found."
        else:
            parsedResult = parseResult(foundIdiom, result)
            #print(parsedResult)
            return parsedResult    
    

def parseResult(idiom, input):

    #The string of examples 
    s = str(input[2].iloc[0])

    #Parse examples into just one 
    string = s[s.find('text: ')+10:s.find('\', ')+1]

    if string == "":
        string = "N/A"

    #Return result, cleaned up 
    result = "Idiom: " + idiom + "\n" \
        "Part of speech: " + input[0].iloc[0] + "\n" + \
        "Definition: " + input[3].iloc[0] + "\n" + \
        "Example: " + string 
    

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
