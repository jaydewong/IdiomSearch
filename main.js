import { python } from "pythonia"; 

//Access main.py - Matches the idioms and finds the definition and examples 

const pythonAccess = await python("./main.py");
let setup = await pythonAccess.setup(); 

let userInput = "on the fence";

let result = await pythonAccess.searchInputInDatabase(userInput); 
console.log(result);

python.exit(); 
 //Result is a string 

//Exit call to main.py 


