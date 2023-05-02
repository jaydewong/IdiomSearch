"""
import idiomatch

main

terminal text input

idiomatch search and return output
"""

import sys
import spacy
from idiomatch import Idiomatcher

def main():
    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher = Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.

    # this always times out on us
    test = input("test input: ")

    while (test != "stop"):
        print(test)
        doc = nlp(test)  # process the sentence with an nlp pipeline
        print(idiomatcher.identify(doc))  # identify the idiom in the sentence
        test = input("test input: ")

    print("Program stopped. "); 

if __name__ == '__main__':
    main()
