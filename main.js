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

//access python idiomatch file 
const searchResult = await python("./main.py");

const userInput = ["this guy is balls out insane", "there will be blood on your hands", "on the fence"]; 

for(let i = 0; i < userInput.length; i++){
    if(i === 0){
        //set up the database
        console.log(await searchResult.setup()); 
        console.log("setup complete"); 
    }
    console.log(await searchResult.is_idiom(userInput[i]));
}

python.exit(); 
