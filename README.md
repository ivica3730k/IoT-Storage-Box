# IoT-Storage-Box
Simple IoT storage project, working inside Docker Container or standalone.
Saving data to sqlite3 database file, with no authentication what so ever.
## How does it work
You store the data using your own API key you specify (must be UUID4).
Do not forget your api key and do not give it to someone else.
## Reading, writing and deleting data
### Writing data to Storage
Currently, only supported way of writing data to the storage is trough
get requests using url arguments (for esp8266 and GSM shields mostly).
You can name your parameters however you want.
Visting url below will save name ivica and surname matic into the Storage:
<http://storageurl/apikeygoeshere/put/?name=ivica&surname=matic>
### Obtaining data from Storage
Visiting url below will give all data points in JSON format stored for provided apikey:
<http://storageurl/apikeygoeshere/get/>

Visting this url would return:
```javascript
{
    "2020-10-24 02:01:47.195710": {
        "name": "ivica",
        "surname": "matic"
    }
}
```
### Deleting data from storage
Visiting url below will erase all data in the Storage for specified api key:
<http://storageurl/apikeygoeshere/remove/>

## Contributing to the project
Fell free to fork version of the code and create your own version and start a pull request.
This is work in progress, so above information might change in future.
