let weather = {
    "apiKey": "2ec3f5814a61b61fe059792bb6d2c417",
    fetchWeather: function () {
        fetch(
            "https://api.openweathermap.org/data/2.5/weather?q=Manchester&units=metric&appid=2ec3f5814a61b61fe059792bb6d2c417"
        ).then((response)=> response.json())
        .then((data) => console.log(data));
    },
    showWeather: function(data) {

    }
};


// change text function
// js events - slide 5 - display date.
// bootstrap to manage nav bar