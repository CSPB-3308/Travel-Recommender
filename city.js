var request = new XMLHttpRequest();
request.open("GET", "./city_list.json", false);
request.overrideMimeType("application/json");
request.send(null);
var jsonData = JSON.parse(request.responseText);

for (const property in jsonData) {
    console.log(jsonData[property])
    var x = document.getElementById('home');
    var option = document.createElement('option');
    option.text = jsonData[property];
    x.add(option);
}
for (const property in jsonData) {
    console.log(jsonData[property])
    var x = document.getElementById('destination');
    var option = document.createElement('option');
    option.text = jsonData[property];
    x.add(option);
}


