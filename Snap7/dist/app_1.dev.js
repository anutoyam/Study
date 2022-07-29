"use strict";

var _require = require('ejs'),
    fileLoader = _require.fileLoader;

var express = require('express');

var plc = require("./plcCon.js");

var DO = require("./dataobject.js");

var fs = require("fs");

var app = express();
var data = new Array();
var count = 0;
var OnOff = true; //CSS Load

app.use(express["static"](__dirname));
app.set('views', __dirname + '/view');
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);
app.get('/', function (req, res) {
  res.render('index', {
    name: 'TEST',
    data1: data[0],
    data2: data[1]
  });
});
app.listen(3000, function () {
  console.log("port 3000");
});
plc.plcConnect();
ReadPlc();

function ReadPlc() {
  var time;
  return regeneratorRuntime.async(function ReadPlc$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.prev = 0;
          _context.next = 3;
          return regeneratorRuntime.awrap(DO.ProccessData());

        case 3:
          data = _context.sent;
          time = newTime();
          fs.writeFileSync("./plcData/" + time[0] + "txt", "[" + time[1] + "]" + data + '\n', {
            flag: 'a+'
          });
          setTimeout(function () {
            if (OnOff = true) {
              console.log("--------" + count + "---------");
              ReadPlc();
              count++;
            } else {
              return;
            }
          }, 1000);
          _context.next = 12;
          break;

        case 9:
          _context.prev = 9;
          _context.t0 = _context["catch"](0);
          return _context.abrupt("return");

        case 12:
        case "end":
          return _context.stop();
      }
    }
  }, null, null, [[0, 9]]);
}

var newTime = function newTime() {
  var today = new Date();
  var date = today.toLocaleDateString();
  var time = today.toLocaleString('en-US');
  return [date, time];
};

process.once('SIGINT', function () {
  OnOff = false;
  plc.plcDisconnect();
  console.log("You've pressed Ctrl + C on this process.");
});