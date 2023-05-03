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

const userInput = ["this guys is balls out insane"]; 

for(let i = 0; i < userInput.length; i++){
    if(i === 0){
        //set up the database
        console.log(await searchResult.setup()); 
        console.log("setup complete"); 
    }

    const result = async () => {
        const isIdiom = await searchResult.is_idiom(userInput[i]); 
      
        return isIdiom; 
    }

    let readResult = await result(); 
    readResult.replaceAll('\'', '"')
    //[{'idiom': 'balls-out', 'span': 'balls out', 'meta': (2876800142358111704, 3, 5)}]

    let resultJSON = JSON.parse(JSON.stringify(readResult));  //turn it into JSON format
    console.log(resultJSON.idiom); 


    //readResult = readResult.replace("\"'idiom'\":", "\"idiom\":");
    // const parsedResult = JSON.parse(readResult);
    // console.log(parsedResult.idiom); 
    //console.log();


    //if the input is an idiom
    // if(result != null){
    //     let idiom = await result(); 
    //     console.log(idiom[0]); 
    // }else{
    //     console.log("not an idiom");
    // }
}


python.exit(); 
