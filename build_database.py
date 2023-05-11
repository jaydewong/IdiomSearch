import pandas as pd

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
    print(type(response))           # 'http.client.HTTPResponse'


    # pandas attempt
    df = pd.read_json(url, orient="records", lines=True)
    print("Database Build complete")
    # print(df.head())
    # print(df.iloc[0])
    # print(df["word"])

def searchDatabase(query):
    #query is currently a list of dictionaries formatted as a JSON string

    #load a list of queries to check in Pandas
    query = json.loads(query)
    queryDf = [item['idiom'] for item in query]
    
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

# senses: examples, synonyms, and glosses (definition)
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
    build()
    search("rain cats and dogs")