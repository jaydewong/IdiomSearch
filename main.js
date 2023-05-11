//"use strict";
//creating a basic project - testing out how to write and compile typescript 
// Object.defineProperty(exports, "__esModule", { value: true });
// exports.idiom_detect = void 0;
// const idiom = 'the world is my oyster';
// function idiom_detect(who = idiom) {
//     return "This is an idiom";
// }
// exports.idiom_detect = idiom_detect;
import { python } from "pythonia"; 


//access main python file 
const pythonMain = await python("./main.py");

const userInput = ["sit on a fence"]; 

//FOR EACH OF THE USER INPUTS
for(let i = 0; i < userInput.length; i++){

    //SET UP DATABASE
    if(i === 0){
        //Set up the Idiomatcher and Pandas Database
        console.log(await pythonMain.setup()); 
    }

    //Get idiom result back from Idiomatcher, search idiom in Pandas database
    let result = await pythonMain.searchInputInDatabase(userInput[i]);
    
    //This result is the part of speech of the idiom, not the definition. edit in build_database -> searchDatabase
    console.log(result)
}


python.exit(); 
