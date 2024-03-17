# KHETALA
Khetala is a crop recommendation service with a primary aim of helping farmers decide which crops to plant based on different factors including yield, soil profile, weather and market price.

Read more about the <a href="https://github.com/Data-Crunch-Team-Green/khetala-server/blob/main/Project%20Description.md">project description here</a>.

## Installation and usage
Clone this repository:
``` sh
$ git clone git@github.com:Data-Crunch-Team-Green/khetala-server.git
```

Install all the libraries:
``` sh
$ pip install -r requirements.txt
```

Start the server:
``` sh
$ uvicorn main:app --reload
```
The server runs on http://127.0.0.1:8000

#### The documentations of the currently available apis can be found at http://127.0.0.1:8000/docs


## Roadmap
◽ Optimize the current ML model to get higher accuracy in predicting crop based on soil profile. Requires more data collection and may also require feature engineering

◽ Collect and add yield, soil and price datasets of all other crops grown in Nepal. Add regional market prices as well. 

◽ Compare the optimal soil profile of the crop with the users soil profile to generate percentage match. Use this to recommend type of fertilizer required for better yield of the crop.

◽ Use weather api and compare the users current weather profile with the optimal weather condition to predict and alert plantation time of the interested crop.



