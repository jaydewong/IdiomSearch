from idiomatch import Idiomatcher
import spacy

#finish building this later

def buildIdiomatcher():
    global nlp
    global idiomatcher

    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher = Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.
    print("Idiomatcher complete")

def matchIdiom(input):
    doc = nlp(input) # process the sentence with an nlp pipeline

    return parseMatchedIdiom(str(idiomatcher.identify(doc)))

def parseMatchedIdiom(input):

    #input comes in as a string 
    input = input.replace("\'", "\"")
    print("2: " +input)
    input = input.split("}, {")
    print(type(input))
    return input

if __name__ == '__main__':
    buildIdiomatcher()