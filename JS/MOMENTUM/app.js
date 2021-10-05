// 이전에는 var를 사용했지만 보호의 여부에따라
// const, let으로 나눠 사용하기로 업데이트함
const a = 5; //상수(변하지 않음)
const b = 6; //상수
let myEmoji = "^^" //가변

console.log(a*b);
console.log(a+b);
console.log(a/b);
console.log("Hello " + "JS NEWBIE" + myEmoji);

myEmoji = "^ㅅ ^";
console.log("Hello " + "JS NEWBIE" + myEmoji);