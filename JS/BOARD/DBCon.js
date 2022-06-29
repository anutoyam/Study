const btn_READ = document.getElementById("db_READ");

const mysql = require('mysql');
const conn = {
    host: '127.0.0.1',
    port: '3306',
    user: 'T_ID',
    password: '1234',
    database: 'test_db'
};

btn_READ.addEventListener("click",selectQuery);

function selectQuery() {
    let connection = mysql.createConnection(conn);
    connection.connect();

    let sql = "select * from tb_user";

    connection.query(sql, function (err, results, fields) {
        if (err) {
            console.log(err);
        }
        console.log(results);
    })

    connection.end();
}
