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
    global run_setup
    global nlp
    global idiomatcher
    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher = Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.
    run_setup = True
    return run_setup

def is_idiom(input):


    doc = nlp(input) # process the sentence with an nlp pipeline
    return idiomatcher.identify(doc)


def main():
    if (not run_setup):
        setup()

    print("Program stopped. "); 

if __name__ == '__main__':
    setup()
    main()
