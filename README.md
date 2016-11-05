# Rate limit API

### Installation requirements:
1. Install pip
2. Install flask

### Run the application:
1. python $PATH/rate_limit_API/api_handler.py   ```(from CLI)```
2. Open http://localhost:5000/  ```(in browser)```

### API endpoints:

#### endpoint: ```https://localhost:5000/getCityHotels```
#### Request Type: POST
##### Body: 
	{"city_id":"Ashburn",
	"sort_type":0,
	"api_key":"gethotels1234"}

##### Response:
```
[
   {
      "CITY":"Ashburn",
      "HOTELID":"22",
      "PRICE":"14000",
      "ROOM":"Sweet Suite"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"21",
      "PRICE":"7000",
      "ROOM":"Deluxe"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"20",
      "PRICE":"4444",
      "ROOM":"Superior"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"17",
      "PRICE":"2800",
      "ROOM":"Deluxe"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"25",
      "PRICE":"1900",
      "ROOM":"Deluxe"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"12",
      "PRICE":"1800",
      "ROOM":"Deluxe"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"7",
      "PRICE":"1600",
      "ROOM":"Deluxe"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"24",
      "PRICE":"1400",
      "ROOM":"Superior"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"3",
      "PRICE":"1300",
      "ROOM":"Sweet Suite"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"5",
      "PRICE":"1200",
      "ROOM":"Sweet Suite"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"10",
      "PRICE":"1100",
      "ROOM":"Superior"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"19",
      "PRICE":"1000",
      "ROOM":"Superior"
   },
   {
      "CITY":"Ashburn",
      "HOTELID":"16",
      "PRICE":"800",
      "ROOM":"Superior"
   }
]
```

###### city_id: ```Name of city present in CSV file```
###### sort_type: ```0 for descending and 1 for ascending order of price in CSV file```

#### Permissible API keys:
```
1. 'gethotels1234'   (rate limit: 1 request in 20 seconds)
2. 'gethotels7890'   (rate limit: 1 request in 15 seconds)
```
