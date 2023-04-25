"""
import idiomatch

main

terminal text input

idiomatch search and return output
"""

import sys
import spacy
from idiomatch import Idiomatcher

run_setup = False

def setup():
    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher = Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.
    run_setup = True

def main():
    if (not run_setup) :
        setup()

    # this always times out on us
    test = input("test input (enter 'stop' to exit): ")

    while (test != "stop"):
        print(test)
        doc = nlp(test)  # process the sentence with an nlp pipeline
        print(idiomatcher.identify(doc))  # identify the idiom in the sentence
        test = input("test input (enter 'stop' to exit): ")

    print("Program stopped. "); 

if __name__ == '__main__':
    setup()
    main()
