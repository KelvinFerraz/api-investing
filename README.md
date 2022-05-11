# API Investing

This API was create to return from library investpy using Flask framework.


## How to start?

Create a enviroment to your dependences:

```
pip install -r requeriments.txt
```

Run the api investing:
```
python api.py
```

you receive the return:
   -  ```Running on http://localhost:5000 (Press CTRL+C to quit)```


## Configuration

This application run in port 5000, for you to change, change in the api.py file line 22 in the port variable


## How to use?

This application has to route:
 - / - return index.html
 - /dividendos - return stock information

 Example with curl:

 ```
 curl -X POST localhost:5000/dividendos -H 'Content-Type: application/json' -d '{"stock":"AAPL","country":"United States","from_date":"01/01/2020","to_date":"01/01/2021"}'
 ```

 ### variables to body

  - stock: set the stock name (APPL, MGLU3 etc...);
  - country: set country (Brazil, United States, etc...);
  - from_date: initial date with this format dd/mm/yy
  - to_date: final date with this format dd/mm/yy

### expected return

```
{"name": "Apple", "historical": [{"date": "02/01/2020", "open": 74.06, "high": 75.15, "low": 73.8, "close": 75.09, "volume": 135647008, "currency": "USD"}, {"date": "03/01/2020", "open": 74.29, "high": 75.14, "low": 74.13, "close": 74.36, "volume": 146536000, "currency": "USD"}, {"date": "06/01/2020", "open": 73.45, "high": 74.99, "low": 73.19, "close": 74.95, "volume": 118579000, "currency": "USD"}, {"date": "07/01/2020", "open": 74.96, "high": 75.22, "low": 74.37, "close": 74.6, "volume": 111511000, "currency": "USD"}, {"date": "08/01/2020", "open": 74.29, "high": 76.11, "low": 74.29, "close": 75.8, "volume": 132364000, "currency": "USD"}, {"date": "09/01/2020", "open": 76.81, "high": 77.61, "low": 76.55, "close": 77.41, "volume": 170486000, "currency": "USD"}, {"date": "10/01/2020", "open": 77.65, "high": 78.17, "low": 77.06, "close": 77.58, "volume": 140868992, "currency": "USD"}, {"date": "13/01/2020", "open": 77.91, "high": 79.27, "low": 77.79, "close": 79.24, "volume": 122087000, "currency": "USD"}, {"date": "14/01/2020", "open": 79.18, "high": 79.39, "low": 78.04, "close": 78.17, "volume": 162614000, "currency": "USD"}
```

