from idiomatch import Idiomatcher
import spacy

#Load patterns from idiomatcher into a database
#Idiom matcher needs an nlp pipeline - currently supports en_core_web_sm only.
#Takes approximately 50 seconds to complete 
def buildIdiomatcher():
    global nlp
    global idiomatcher

    print("inside idiomatcher")

    nlp = spacy.load("en_core_web_sm") 
    idiomatcher = Idiomatcher.from_pretrained(nlp) 
    print("Idiomatcher patterns have been loaded.")

#Takes in a phrase and returns a list of possible idiom matches for that phrase. 
def matchIdiom(input):

    #Process the phrase with an nlp pipeline
    doc = nlp(input) 
    idiomList = parseMatchedIdiom(str(idiomatcher.identify(doc)))

    return idiomList

#Takes in the raw result of a matched idiom and formats it into a JSON string
def parseMatchedIdiom(input):

    #replace ' with " for proper JSON format 
    input = input.replace("{\'", "{\"") #handle {'
    input = input.replace("\':", "\":") #handle ':
    input = input.replace(" \'", " \"") #handle space'
    input = input.replace("\',", "\",") #handle ',

    #replace ) or ( with )" and "( for proper JSON format 
    #allows the original tuple for metadata to be read as a string
    input = input.replace("(", "\"(")
    input = input.replace(")", ")\"")

    return input

if __name__ == '__main__':
    buildIdiomatcher()