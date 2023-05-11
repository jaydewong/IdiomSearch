from idiomatch import Idiomatcher

#finish building this later

def buildIdiomatcher():
    nlp = spacy.load("en_core_web_sm")  # idiom matcher needs an nlp pipeline; Currently supports en_core_web_sm only.
    idiomatcher = Idiomatcher.from_pretrained(nlp)  # this will take approx 50 seconds.
    print("Idiomatcher complete")