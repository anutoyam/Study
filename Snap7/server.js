var snap7 = require('node-snap7');

var s7client = new snap7.S7Client();
s7client.ConnectTo('192.168.0.95',0,2,function(err){
    if(err)
    return console.log('>> Connection failed. Code #' + err + ' - ' + s7client.ErrorText(err));

    s7client.DBRead(58,20,8,function(err, res){
        if(err)
        return console.log('>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err));

        console.log(res);
    });
});

s7client.Disconnect();