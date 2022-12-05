import requests
import json
#from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://github.com/keady-r/Programming_for_DA'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = ["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"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)