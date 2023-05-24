import pandas as pd
import re

# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as parameter for urlopen
url = "https://kaikki.org/dictionary/English/tag/tagged-idiomatic/kaikki_dot_org-dictionary-English-tagged-idiomatic.json"


def buildDatabase():
    global df

    # store response of URL
    response = urlopen(url)
    # print(type(response))   # 'http.client.HTTPResponse'

    # pandas attempt
    df = pd.read_json(url, orient="records", lines=True)

    # synonyms
    senses = df["senses"].where(df["senses"].notna())
    synonyms = senses.apply(lambda x: (re.findall(r"'synonyms': (\[\{.+?\}\])", str(x))))
    synonyms = synonyms.apply(lambda x: x[0] if len(x) > 0 else None).dropna()
    df["synonyms"].fillna(value=synonyms, inplace=True)

    # examples
    df["examples"] = senses.apply(lambda x: (re.findall(r"'examples': (\[\{.*?\}\])", str(x))))
    df["examples"] = df["examples"].apply(lambda x: x[0] if len(x) > 0 else None)

    # glosses
    df["glosses"] = senses.apply(lambda x: (re.findall(r"'glosses': (\[.*?\])", str(x))))
    df["glosses"] = df["glosses"].apply(lambda x: x[0] if len(x) > 0 else None)

    print("Build definition database complete")


def searchDatabase(query):
    #query as input is a list of dictionaries formatted as a JSON string

    #Load a list of queries to check in Pandas
    query = json.loads(query)
    queryDf = [item['idiom'] for item in query]
    
    #Print the list of found matched idioms from Idiomatcher
    print(queryDf)

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

            return [possibleMatch.pos, possibleMatch.synonyms, 
                      possibleMatch.examples, possibleMatch.glosses]
            
            #return possibleMatch.senses[4] #tried accessing glosses 

# senses: examples, synonyms, and glosses (definition); recursive search for synonyms?
# extract into new column
# rain cats and dogs -> rain dogs and cats

# blend (?) alternative forms
    # rain cats and dogs | rain dogs and cats
    # have another thing coming | have another think coming
    # ass-backwards
    # cut a swath | cut a wide swath
# glosses -> alternative forms -> df[alternative forms -> combine rows -> search alternative forms


if __name__ == '__main__':
    buildDatabase()
    print(df.iloc[0])
    print(df.iloc[0]["examples"])
    searchDatabase("rain cats and dogs")
    print(df.loc[10])