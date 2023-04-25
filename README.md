# IdiomSearch

Main-Jayde: testing using typescript and python together 

Install Typescript: npm i typescript --save-dev
Install JSPyBridge: npm install pythonia
Install Idiomatch: pip3 install idiomatch
Install Spacey: python3 -m spacy download en_core_web_sm

Compile TS: npm run compile 
Run Single JS file: node main-jayde.js

If you run into an issue pushing to git because a stream wasn't closed cleanly, 
try git config http.postBuffer 524288000 and push again. 

Notes: 
Our python program ends when we don't supply input and we have leaked objects to clean up