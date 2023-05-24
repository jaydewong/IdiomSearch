# IdiomSearch

main.js: testing using typescript and python together; process user input to extract idiom
main.py: idiomatch setup and user input
build_database.py: 
    - buildDatabase(): pull json file of idiom definitions and convert to Pandas dataframe
    - searchDatabase(query): search database for query of idioms and return structured output 

Install Typescript: npm i typescript --save-dev
Install JSPyBridge: npm install pythonia
Install Idiomatch: pip3 install idiomatch
Install Spacey: python3 -m spacy download en_core_web_sm
Install Pandas: pip3 install pandas

Compile TS: npm run compile 
Run Single JS file: node main-jayde.js

If you run into an issue pushing to git because a stream wasn't closed cleanly, 
try git config http.postBuffer 524288000 and push again. 

Notes: 
- BridgeException occurs since py file isn't returning anything to JS, as we're 
staying in a while loop. Need to fix, but if we call py file once for each word 
we search up, we have to initialize Idiomatcher every time and it takes too long