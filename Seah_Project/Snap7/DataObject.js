//constructor
let result = new Array(52);

const wordLengh = 48;
const boolLengh = 4;

const plc = require("./plcCon.js")

module.exports = {
    ProccessData: async function () {
        result = await plc.plcRead();

        //Word Data Read
        let arrWord = new Array(24);
        for (let i = 0; i < wordLengh / 2; i++) {
            //Word를 Read하기에 0,1.. 번째 값을 hex -> dec 후에 bin으로 변환(tostring)후에 합침
            arrWord[i] = [
                result[i * 2].toString(2),
                result[i * 2 + 1].toString(2)
            ];
            //8자리 빈공간에 0을 채움
            arrWord[i] = arrWord[i].map(fillZero);
            // 8비트 배열 2개를 합침(16비트)
            arrWord[i] = arrWord[i].join('');
            //bin을 dec로 변환
            arrWord[i] = parseInt(arrWord[i], 2);
            //최상위 비트 확인 후 음수로 변경
            if ((arrWord[i] & 0x8000) > 0) {
                arrWord[i] = arrWord[i] - 0x10000;
            }
        }
        let arrBool = new Array(32);
        let arrBit = new Array(32);
        for (let i = 0; i < boolLengh; i++) {
            //3차 정리
            arrBool[i] = result[i + wordLengh].toString(2);
            arrBool[i] = fillZero(arrBool[i]);
            arrBool[i] = arrBool[i]
                .split('')
                .reverse();
            arrBool[i] = arrBool[i].join('');

            // const bin = res[i].toString(2); 1차 시도 실패 fillZero(bin);
            // arrBit.push(...bin.split("").reverse()); 2차 시도 성공 - 이렇게 해야 가능 zeroBin
            // =fillZero(bin); arrBit.push(...zeroBin.split("").reverse());
        }
        arrBool = arrBool.join('');
        arrBit = arrBool.split('')
        arrBool = arrBit.map(boolFromStringOtherwiseNull);
        return [arrBool, arrWord];     
    }
}

function boolFromStringOtherwiseNull(s) {
    if (s == '1') 
        return true
    if (s == '0') 
        return false
    return null
}

//Empty Space Fill Zero
function fillZero(data) {
    if (data.length !== 8) {
        const zero = "0";
        const zeroLength = 8 - data.length;
        for (let i = 0; i < zeroLength; i++) {
            data = zero + data;
        }
    }
    return data;
}

