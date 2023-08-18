# JSON = JavaScript Object Notation

# json.dump()  - Write
# json.load()  - Read
# json.update()  - Update

import json

data = {
    "Key": {
        "Reference 1": "Value 1",
        "Reference 2": "Value 2",
    }
}

with open(file = "./Day_30_Errors,_Exceptions_and_JSON_Data_Improving_the_Password/data.json", mode = 'a') as data_file:
    json.dump(data, data_file)