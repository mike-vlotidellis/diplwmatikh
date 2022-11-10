import json
print ("hello word")
with open('states2.json') as f:
  data = json.load(f)

for state in data['states']:
  print (state['name'])