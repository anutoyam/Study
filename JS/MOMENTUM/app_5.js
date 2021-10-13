const calculator = {
    add: function (a, b) {
        return a + b;
    },
    minus: function (a, b) {
        return a - b;
    },
    divide: function (a, b) {
        return a / b;
    },
    square: function (a, b) {
        return a ** b;
    }
}
const addResult = calculator.add(6,77);
const minusResult = calculator.minus(6,77);
const divideResult = calculator.divide(6,77);
const squareResult = calculator.square(6,10);