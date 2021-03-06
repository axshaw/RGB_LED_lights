var express = require('express');
var app = express();
var exec = require('child_process').exec;

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', function (req, res, next) {

	exec("/home/pi/kidsLights/getLights.sh", function(error, stdout, stderr) {
		if(!error)	{

			res.json(stdout.replace(/\r?\n|\r/,"").split(" "));
		}else	{
			res.status(500).json({error:error});
		}
	});

})

app.get('/setColour/:red-:green-:blue', function(req, res, next) {
  exec("/home/pi/kidsLights/changeLights.sh " + req.params['red'] + " " + req.params['green'] + " " + req.params['blue'], function(error, stdout, stderr) {
		if(!error)	{
			res.status(200).send(req.params['red'] + " " + req.params['green'] + " " + req.params['blue']);
		}else	{
			res.status(500).json({error:error});
		}
	});
})

app.listen(3010, function()	{
	console.log('running on 3010')
})
