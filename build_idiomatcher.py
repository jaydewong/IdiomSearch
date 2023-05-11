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

    #input comes in as a string 

    #replace ' with " for proper JSON format 
    input = input.replace("\'", "\"")

    #replace ) or ( with " for proper JSON format 
    input = input.replace("(", "\"(")
    input = input.replace(")", ")\"")


    #replace }, { with }/ { for easier split 
    #input = input.replace("}, {", "}/ {")

    #erase beginning and end brackets 
    #input = input[1:-1]
    
    #split input into indiividual idiom matches 
    #input = input.split("/ ")

    #check output 
    #print(type(input))
    #print("Item 1: " + input[0])
    #print("Item 2: " + input[1])
    return input

if __name__ == '__main__':
    buildIdiomatcher()