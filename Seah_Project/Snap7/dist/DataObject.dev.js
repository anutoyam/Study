"use strict";

//constructor
var result = new Array(52);
var wordLengh = 48;
var boolLengh = 4;

var plc = require("./plcCon.js");

module.exports = {
  ProccessData: function ProccessData() {
    var arrWord, i, arrBool, arrBit, _i;

    return regeneratorRuntime.async(function ProccessData$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            _context.next = 2;
            return regeneratorRuntime.awrap(plc.plcRead());

          case 2:
            result = _context.sent;
            //Word Data Read
            arrWord = new Array(24);

            for (i = 0; i < wordLengh / 2; i++) {
              //Word를 Read하기에 0,1.. 번째 값을 hex -> dec 후에 bin으로 변환(tostring)후에 합침
              arrWord[i] = [result[i * 2].toString(2), result[i * 2 + 1].toString(2)]; //8자리 빈공간에 0을 채움

              arrWord[i] = arrWord[i].map(fillZero); // 8비트 배열 2개를 합침(16비트)

              arrWord[i] = arrWord[i].join(''); //bin을 dec로 변환

              arrWord[i] = parseInt(arrWord[i], 2); //최상위 비트 확인 후 음수라면 음수로 변경

              if ((arrWord[i] & 0x8000) > 0) {
                arrWord[i] = arrWord[i] - 0x10000;
              }
            }

            arrBool = new Array(32);
            arrBit = new Array(32);

            for (_i = 0; _i < boolLengh; _i++) {
              //3차 정리
              arrBool[_i] = result[_i + wordLengh].toString(2);
              arrBool[_i] = fillZero(arrBool[_i]);
              arrBool[_i] = arrBool[_i].split('').reverse();
              arrBool[_i] = arrBool[_i].join(''); // const bin = res[i].toString(2); 1차 시도 실패 fillZero(bin);
              // arrBit.push(...bin.split("").reverse()); 2차 시도 성공 - 이렇게 해야 가능 zeroBin
              // =fillZero(bin); arrBit.push(...zeroBin.split("").reverse());
            }

            arrBool = arrBool.join('');
            arrBit = arrBool.split('');
            arrBool = arrBit.map(boolFromStringOtherwiseNull);
            return _context.abrupt("return", [arrBool, arrWord]);

          case 12:
          case "end":
            return _context.stop();
        }
      }
    });
  }
};

function boolFromStringOtherwiseNull(s) {
  if (s == '1') return true;
  if (s == '0') return false;
  return null;
} //Empty Space Fill Zero


function fillZero(data) {
  if (data.length !== 8) {
    var zero = "0";
    var zeroLength = 8 - data.length;

    for (var i = 0; i < zeroLength; i++) {
      data = zero + data;
    }
  }

  return data;
}