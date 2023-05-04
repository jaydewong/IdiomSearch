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

/**NOTES
 * 
 * this parsing only works if idiomatcher returns one matched idiom. i think it might be 
 * better to move the parsing into python and make it proper JSON format before returning it to this JS file
 * 
 * */



//access python idiomatch file 
const searchResult = await python("./main.py");

//ISSUE - matches to multiple idioms??
//const userInput = ["you're gonna have blood on your hands if you do this"]; 
//{"idiom": "have someone going", "span": ""re gon na have", "meta": "18378485065316437412, 1, 5"}, {"idiom": "have someone going", "span": "you "re gon na have", "meta": "18378485065316437412, 0, 5"}, {"idiom": "have blood on one"s hands", "span": "have blood on your hands", "meta": "5930902300252675198, 4, 9"}, {"idiom": "on one"s hands", "span": "on your hands", "meta": "8246625119345375174, 6, 9"}

const userInput = ["fence"]; //current implementation only works if idiomatcher matches it to ONE idiom, not multiple 

//FOR EACH OF THE USER INPUTS
for(let i = 0; i < userInput.length; i++){

    //SET UP DATABASE
    if(i === 0){
        //set up the database
        console.log(await searchResult.setup()); 
        console.log("setup complete"); 
    }

    //CALL PYTHON API 
    const result = async () => {
        const isIdiom = await searchResult.is_idiom(userInput[i]); 
      
        return isIdiom; 
    }

    let readResult = await result(); 
    console.log(typeof readResult); 

    //PARSE IDIOMATCH DATA - ASSUMING WE RECEIVE A STRING 
    if(readResult != "[]"){
        readResult = readResult.replace(/'/g, '"').replace(/\(/g, '"').replace(/\)/g, '"'); 
        readResult = readResult.substring(1, readResult.length-1); 

        console.log(readResult); 

        let parsedResult = JSON.parse(readResult);
        console.log(parsedResult.idiom); 



    }else{
        console.log("idiom not identified"); 
        //add some kind of break here?
    }

}


python.exit(); 
