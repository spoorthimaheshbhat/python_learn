import json

given_json = '{"city":"London","country":"UK"}'

location = json.loads(given_json)
print(location)
print(type(location))