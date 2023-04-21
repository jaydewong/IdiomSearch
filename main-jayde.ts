//creating a basic project - testing out how to write and compile typescript 

//for this section to work you have to run with "node main-jayde.ts"
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
  });

readline.question(`Give me an idiom?`, idiom => {
  console.log(`Hi ${idiom}!`);
  readline.close();
});

/*export function idiom_detect(who: string | null = idiom): string {

    return "This is an idiom";
}*/

