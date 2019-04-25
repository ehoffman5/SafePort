// declaring JSON variables
var fs = require('fs');
var readData = fs.readFileSync('src/js/results.json');
var results = JSON.parse(readData);

console.log(results);

var runFull = document.getElementById("runFull")

// add event listener for scan button click
runFull.addEventListener('click', function() {
    // open loading screen
    document.getElementById("load_screen").style.display = "block";

    // run python script
    var python = require('child_process').spawn('python', ['src/python/full.py']);

    python.stdout.on('data', function(data){

        console.log("data: ",data.toString('utf8'));

        // store results in JSON
        results = data.toString('utf8');
        var writeData = JSON.stringify(results);
        fs.writeFile('src/js/results.json', writeData, (err) => {
            if (err)
                throw err;
            else  // move window to results page
                document.location.href = "../html/results.html";
        });
    });
});