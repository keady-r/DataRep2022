#To do: Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

import requests
import json
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

response = requests.get(url)
data = response.json()
print(data)

with open("dataOutput.json", "w") as fp:
    json.dump(data, fp)
        