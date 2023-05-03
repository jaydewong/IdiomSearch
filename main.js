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
//print out result of calling function - runs idiomatch 
console.log(await searchResult.main()); 
python.exit(); 