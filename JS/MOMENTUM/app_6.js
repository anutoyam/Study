//const age = 96;
// function calculatorKrAge(ageOfForeigner) {
//     return ageOfForeigner + 2;
// }

// const krAge = calculatorKrAge(age);

const age = prompt("How old are you?"); //멈춰서 사용자의 응답을 기다림
// console.log(isNaN(age));

if(isNaN(age)){
    console.log("Please write a number");
}else if(age < 18){
    console.log("You are too young");
}else if(age>= 18 && age <= 50){
    console.log("You can drink");
}else{
    console.log(isNaN(age) +"? "+"Thank you for writing your age.");
}
