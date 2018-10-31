require('dns').resolve('www.google.com', function(err) {
  if (err) {
       console.log("No connection");
         } else {

                'use strict';
                var request = require('request');

                //Go get you an api code from api.darksky.net
                var url = 'https://api.darksky.net/forecast/53471ed8c7937bb735401d5f71dfb0d2/44.052151,-123.091187';

                request.get({
                    url: url,
                    json: true,
                    headers: {'User-Agent': 'request'}
                   }, (err, res, data) => {
                    if (err) {
                       console.log('Error:', err);
                    } else if (res.statusCode !== 200) {
                       console.log('Status:', res.statusCode);
                      } else {
                        // data is already parsed as JSON:
                       var summary = (data.currently.summary);
                       var temp_suffix = (data.currently.temperature + "°F",  data.currently.summary);

                       if (summary === "Cloudy" || summary === "Partly Cloudy" || summary === "Mostly Cloudy" || summary === "Light Rain") {
                       console.log("☁" + " " + data.currently.temperature + "°F",  data.currently.summary);
                       }

                       else if (summary === "Rain" || summary === "Heavy Rain" || summary === "Light Rain") {
                       console.log("☔" + " " + data.currently.temperature + " F",  data.currently.summary);
                       }

                       else if (summary === "Sunny") {
                       console.log("☼" + " " + data.currently.temperature + "°F",  data.currently.summary);
                       }

                       else if (summary === "Light Snow" || summary === "Flurries" || summary === "Snow") {
                       console.log("❄" + " " + data.currently.temperature + "°F",  data.currently.summary);
                       }

                       else if (summary === "Clear") {
                       console.log("" + " " + data.currently.temperature + "°F",  data.currently.summary);
                       }

                       else {
                       //console.log("your mom! Look at the code");
                       console.log("wingnut" + " " + data.currently.temperature + "°F", "\n" + data.currently.summary);
                       }

                     }
                });
                }
                });
