var express = require('express');
var app = express();
var exec = require('child_process').exec;

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', function (req, res, next) {
	res.send(200)

})

app.get('/barnack/currentTemp' function (req, res, next)	{
	res.send(200)
})


app.listen(3011, function()	{
	console.log('running on 3011')
})
