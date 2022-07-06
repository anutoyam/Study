const express = require('express');
const fs = require('fs');
const ejs = require('ejs');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const {isBuffer} = require('util');

const client = mysql.createConnection(
    {user: 'root', password: '1234', database: 'test_db'}
);

const app = express();

app.use(express.static(__dirname));
//app.use('/css',express.static(__dirname +'/css'));

app.use(bodyParser.urlencoded({extended: false}));

app.listen(52273, function () {
    console.log('Server is running at : http://127.0.0.1:52273')
});

app.get('/', function (req, res) {
    fs.readFile('list.ejs', 'utf8', function (err, data) {
        client.query('select * from topic', function (err, results) {
            if (err) {
                res.send(err)
            } else {
                res.send(ejs.render(data, {data: results}))
            }
        })
    })
});

app.get('/delete/:id', function (req, res) {
    client.query('delete from topic where id = ?', [req.params.id], function () {
        res.redirect('/');
    })
});

app.get('/insert', function (req, res) {
    fs.readFile('insert.html', 'utf8', function (err, data) {
        res.send(data);
    })
});

app.post('/insert', function (req, res) {
    const body = req.body;

    client.query(
        'insert into topic(title,description,created,author_id) values(?,?,NOW(),?);',
        [
            body.title, body.description, body.author_id
        ],
        function () {
            res.redirect('/');
        }
    );
});

app.get('/edit/:id', function (req, res) {
    fs.readFile('edit.ejs', 'utf8', function (err, data) {
        client.query(
            'select * from topic where id = ?',
            [req.params.id],
            function (err, results) {
                res.send(ejs.render(data, {data: results[0]}));
            }
        );
    });
});

app.post('/edit/:id', function (req, res) {
    const body = req.body;

    client.query(
        'update topic SET title = ?, description = ?, author_id = ? where id = ?',
        [
            body.title, body.description, body.author_id, req.params.id
        ],
        function () {
            res.redirect('/');
        }
    );
});
