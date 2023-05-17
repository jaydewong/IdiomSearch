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
    print(type(response))   # 'http.client.HTTPResponse'


    # pandas attempt
    df = pd.read_json(url, orient="records", lines=True)

    # synonyms
    senses = df["senses"].where(df["senses"].notna())
    synonyms = senses.apply(lambda x: (re.findall(r"'synonyms': (\[\{.+\}\])", str(x))))
    synonyms = synonyms.apply(lambda x: x[0] if len(x) > 0 else None).dropna()
    df["synonyms"].fillna(value=synonyms, inplace=True)

    # print(str(test.iloc[8481]))
    # print(re.findall(r"'synonyms': (\[\{.+\}\])", str(test.iloc[0])))

    # examples
    df["examples"] = senses.apply(lambda x: (re.findall(r"'examples': (\[\{.+\}\])", str(x))))
    df["examples"] = df["examples"].apply(lambda x: x[0] if len(x) > 0 else None)

    # glosses
    df["glosses"] = senses.apply(lambda x: (re.findall(r"'glosses': (\[\{.+\}\])", str(x))))
    df["glosses"] = df["glosses"].apply(lambda x: x[0] if len(x) > 0 else None)

    print(df.columns)

    print("Build complete")
    # print(df.head())
    # print(df.iloc[0])
    # print(df["word"])

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
            print(possibleMatch)

            #return the column of parts of speech of that matched idiom
            print(type(possibleMatch.senses))
            return possibleMatch.pos 
            
            #return possibleMatch.senses[4] #tried accessing glosses 
            #print(possibleMatch.iloc[0].pos)


# senses: examples, synonyms, and glosses (definition); recursive search for synonyms?
# extract into new column
# rain cats and dogs -> rain dogs and cats

"""
# byte -> str -> list attempt
raw_data = response.read()    # read into bytes
str_data = str(raw_data)      # convert bytes to str

# separated by '{"pos":'
print("\\\\n")
data_list = str_data.split('{"pos":')
print(len(data_list))

data = []
with response.read() as f:
    for line in f:
        print(line)

# store JSON response from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)
"""

if __name__ == '__main__':
    buildDatabase()
    searchDatabase("rain cats and dogs")
    print(df.loc[10])