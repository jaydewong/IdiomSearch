# IdiomSearch

Given a phrase, IdiomSearch will identify an idiom if it exists in the phrase using Kim Eunbin's Idiomatch. If an idiom is identified, IdiomSearch will parse Wiktextract's idiom dictionary and output the idiom's part of speech, definition, and examples 

To run the program: 
Run 'node main.js' from console to run the program with the given input in main.js
Run 'python3 main.python' from console to add your own inputs. 

Currently this program can only be run from console, but a browser interface is in progress. 

Citations:

Tatu Ylonen: Wiktextract: Wiktionary as Machine-Readable Structured data, Proceedings of the 13th Conference on Language Resources and Evaluation (LREC), pp. 1317-1325, Marseille, 20-25 June 2022.
https://kaikki.org

Kim Eubin (19 September 2021). Idiomatch. An implementation of SpaCy(3.0)'s Matcher specifically designed for identifying English idioms. https://github.com/eubinecto/idiomatch

