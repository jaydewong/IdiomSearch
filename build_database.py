import pandas as pd
import re
import threading

# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as parameter for urlopen
url = "https://kaikki.org/dictionary/English/tag/tagged-idiomatic/kaikki_dot_org-dictionary-English-tagged-idiomatic.json"


def buildDatabase():
    global df

    # pandas attempt
    dfKeepCols = ["word", "pos", "senses", "synonyms", "antonyms", "translations"]
    df = pd.read_json(url, orient="records", lines=True).loc[:, dfKeepCols]

    # parallelize column builds
    senses = df["senses"]
    synonymsPat = r"'synonyms': \[(\{.+?\})\]"
    examplesPat = r"'examples': \[(\{.*?\})\]"
    glossesPat = r"'glosses': \[(.*?)\]"

    t1 = threading.Thread(target=extractExistingCol(senses, "synonyms", synonymsPat))
    t2 = threading.Thread(target=extractNewCol(senses, "examples", examplesPat))
    t3 = threading.Thread(target=extractNewCol(senses, "glosses", glossesPat))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # alternative forms
    alts = df["glosses"].where(df["glosses"].str.contains("Alternative form of"))
    altsPat = r"Alternative form of (.+?)\.*'"
    extractNewCol(alts, "alternative form", altsPat)

    df = df.set_index(keys="word", drop=False)

    # merge alternative forms
    altKeepCols = ["word", "synonyms", "examples", "alternative form"]
    isAlt = df.loc[:, altKeepCols].dropna(subset="alternative form")    # idioms that are an alternative form
    alternates = isAlt["word"].to_list()
    isAlt = isAlt.set_index("alternative form").rename(columns={"word": "alternative form"})

    df = df.drop(columns="alternative form").drop(index=alternates)
    df = df.merge(isAlt, how="left", left_index=True, right_index=True)
    mergeCols = (lambda x, y: "[" + x + ", " + y + "]" if (type(x) is str and type(y) is str) 
                                else ("[" + x + "]" if type(x) is str 
                                      else ("[" + y + "]") if type(y) is str else y))
    df["synonyms"] = df.apply(lambda z: mergeCols(z["synonyms_x"], z["synonyms_y"]), axis=1)
    df["examples"] = df.apply(lambda z: mergeCols(z["examples_x"], z["examples_y"]), axis=1)
    df = df.drop(columns=["synonyms_x", "synonyms_y", "examples_x", "examples_y"])

    # filter examples
    filterPat = re.compile(r"\{'text': 'For quotations .+?'\}[, \}]?")
    df["examples"] = [filterPat.sub("", x) if type(x) == str else x for x in df["examples"]]
    
    print("Build definition database complete")


def extractExistingCol(source, colName, colPattern):
    series = source.apply(lambda x: (re.search(colPattern, str(x))))
    series = series.apply(lambda x: x.group(1) if x else float("nan")).dropna()
    df[colName].fillna(value=series, inplace=True)

def extractNewCol(source, colName, colPattern):
    df[colName] = source.apply(lambda x: (re.search(colPattern, str(x))))
    df[colName] = df[colName].apply(lambda x: x.group(1) if x else float("nan"))



def searchDatabase(query):
    #query as input is a list of dictionaries formatted as a JSON string

    #Load a list of queries to check in Pandas
    #print(query)
    query = json.loads(query)
    queryDf = [item['idiom'] for item in query]
    
    #Print the list of found matched idioms from Idiomatcher
    #print(queryDf)

    #Check queries in Pandas database 
    #For each query in queryDf
    for q in queryDf: 
        #Check if any column words in Pandas database match the query 
        possibleMatch = df[df["word"].str.contains(q)]
        #possibleMatch is type <class 'pandas.core.frame.DataFrame'>

        if possibleMatch.empty == True:
            continue
        else: 
            #print(possibleMatch)

            return q, [possibleMatch.pos, possibleMatch.synonyms, 
                      possibleMatch.examples, possibleMatch.glosses]
            
            #return possibleMatch.senses[4] #tried accessing glosses 

    #If we reach here, no match was found
    return None, None



if __name__ == '__main__':
    buildDatabase()
    print(df.loc["rain cats and dogs"])
    print(df.loc["cut a wide swath"])
