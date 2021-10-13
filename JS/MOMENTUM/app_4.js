//function

// function sayHello(nameOfPerson, age){
//     console.log("Hello! My name is " + nameOfPerson
//     + " and I'm " + age);
// }
// function plus(a,b){
//     console.log("두 수의 합은 "+ [a + b] + "입니다.")
// }

// function divide(a,b){
//     console.log("두 수의 나눗셈은 "+ [a / b] + "입니다.")
// }

const player = {
    sayHello : function(nameOfPerson, age){
        console.log("Hello! My name is " + nameOfPerson + " and I'm " + age);
    },
    plus : function(a,b){
        console.log("두 수의 합은 "+ [a + b] + "입니다.")
    },
    divide : function(a,b){
        console.log("두 수의 나눗셈은 "+ [a / b] + "입니다.")
    }
}

const calculator = {
    add : function(a, b){
        console.log(a + b);
    },
    divide : function(a, b){
        console.log(a / b);
    }
}
player.sayHello("Tuna",30);
player.sayHello("Summers",21);
player.sayHello("Marino",15);
player.plus(10,20);
player.divide(98,20);

calculator.add(5,8);

