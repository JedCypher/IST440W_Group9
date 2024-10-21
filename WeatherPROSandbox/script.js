fetch("WeatherAPI_Output.json")
.then(function (response){
    return response.json();
})
.then(function (WeatherAPI_Output){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let WeatherAPI_Output of WeatherAPI_Output){
        out += '' +
            '<tr>' +
                '<td>${WeatherAPI_Output.temp}</td>' +
                '<td>${WeatherAPI_Output.humidity}</td>' +
                '<td>${WeatherAPI_Output.description}</td>' +
                '<td>${WeatherAPI_Output.weather</td>' +
                '<td>${WeatherAPI_Output.name</td>' +
                '<td>${WeatherAPI_Output.state}</td>' +
            '</tr>'



    }
    placeholder.innerHTML = out;
})

