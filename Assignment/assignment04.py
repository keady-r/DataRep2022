# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.


import requests
import json

filename = "repo-public.json"
url = "https://api.github.com/repos/keady-r/data-representation-coursework"

response = requests.get(url)
print(response.status_code)
repoJSON = response.json()


with open (filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)