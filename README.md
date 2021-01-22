  IoT Storage Box

IoT-Storage-Box
===============

Simple IoT storage project, working inside Docker Container or standalone. Saving data to sqlite3 database file, with no authentication what so ever.

* * *

How does it work
----------------

You store the data using your own API key you specify (must be UUID4). Do not forget your api key and do not give it to someone else.

Example of UUIDv4 Api Key which you can use: **eccf62e9-66e4-47ad-8a2f-511c67f1e85c**

Reading, writing and deleting data
----------------------------------

* * *

### Writing data to Storage

Currently, only supported way of writing data to the storage is trough get requests using url arguments (for esp8266 and GSM shields mostly).  
You can name your parameters however you want. Visiting url below will save name "ivica" and surname "matic" into the Storage:

[https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/put/?name=ivica&surname=matic](https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/put/?name=ivica&surname=matic)

### Obtaining data from Storage

Visiting url below will give all data points in JSON format stored for provided apikey:

[https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/get/](https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/get/)

Visting this url would return:

    {
        "1": {
            "name": "ivica",
            "surname": "matic",
            "timestamp": "2020-10-24 02:01:47.195710"
        }
    }
    

### Deleting data from Storage

Visiting url below will erase all data in the Storage for specified api key:

[https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/remove/](https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/remove/)

You can also delete a single data point by specifying a entry id in addition to api key:

[https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/remove/1](https://localhost:8080/eccf62e9-66e4-47ad-8a2f-511c67f1e85c/remove/)

* * *

### Note

This service is set up to support both HTTP and HTTPS requests.

* * *

Contributing to the project
---------------------------

Fell free to fork version of the code and create your own version and start a pull request. This is work in progress. All information above might change in the future.  
  
You can find source code at [https://github.com/ivica3730k/IoT-Storage-Box](https://github.com/ivica3730k/IoT-Storage-Box)

* * *

Disclaimer
----------

**There is nothing preventing me or someone else from seeing your data!** Even if UUIDv4 is almost impossible to guess it can happen. And also, your data is saved in the readable text format. Do not put any data you would not want to share with someone else. I am taking no responsibility what so ever for you or your data.