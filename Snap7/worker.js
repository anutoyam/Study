var snap7 = require('node-snap7');
var s7client = new snap7.S7Client();
var i = null;

function plcConnect(){
    s7client.ConnectTo('192.168.0.95',0,2,isconnecting);
} 

function plcDisConnect(){
    s7client.Disconnect();
}



// 메시지 수신
self.onmessage = function( e ) {
    loop();
};

// 호출한 페이지에 1씩 증가시킨 i를 1초마다 전달한다.
function loop() {
    plcConnect();

    s7client.DBRead(58,20,8,function(err, res){
        if(err)
        return console.log('>> DBRead Failed. Code #' + err + ' - ' + s7client.ErrorText(err));
        
        for (let a = 0; a < res.length; a++) {
            i = res[a]; 
            postMessage(i); 
        }    
    });

    plcDisConnect();
    
    

    // 1초뒤에 다시 실행
    setTimeout( function() {
        loop();
    }, 1000 );

}