import pandas as pd

# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as parameter for urlopen
url = "https://kaikki.org/dictionary/English/tag/tagged-idiomatic/kaikki_dot_org-dictionary-English-tagged-idiomatic.json"


def build():
    global df

    # store response of URL
    response = urlopen(url)
    print(type(response))           # 'http.client.HTTPResponse'


    # pandas attempt
    df = pd.read_json(url, orient="records", lines=True)
    # print(df.head())
    # print(df.iloc[0])
    # print(df["word"])

def search(query):
    print(query)
    matches = df[df["word"].str.contains(query)]
    print(matches)
    print(matches.iloc[0])
    # print(df[df["word"] == query])

build()
search("on the fence")

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