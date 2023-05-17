import { python } from "pythonia"; 

//Access main.py - Matches the idioms and finds the definition and examples 
const pythonMain = await python("./main.py");

//Input a list of phrases to try to match as an idiom - will eventually be replaced 
//with input from the browser and the user's selection 
const userInput = ["sit on the fence"]; 

//For each of the user inputs, match it to an idiom if possible and find the definition and examples
for(let i = 0; i < userInput.length; i++){

    //Set up databases on the first user input - idiom matching patterns and definitions 
    if(i === 0){
        console.log(await pythonMain.setup()); 
    }

    //Match and search for idiom definition if it exists 
    let result = await pythonMain.searchInputInDatabase(userInput[i]);
    
    console.log("Result of idiom matching: " + result)
}

//Exit call to main.py 
python.exit(); 
