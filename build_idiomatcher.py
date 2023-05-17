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
    idiomList = parseMatchedIdiom(str(idiomatcher.identify(doc)))

    return idiomList

#returns a valid JSON string
def parseMatchedIdiom(input):
    #input comes in as a string not formatted in JSON

    #replace ' with " for proper JSON format 
    input = input.replace("\'", "\"")

    #replace ) or ( with )" and "( for proper JSON format - the tuple of metadata 
    input = input.replace("(", "\"(")
    input = input.replace(")", ")\"")

    return input

if __name__ == '__main__':
    buildIdiomatcher()