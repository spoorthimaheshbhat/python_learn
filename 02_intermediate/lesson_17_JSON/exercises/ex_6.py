import json

# Creates a dictionary - data
data = {
    "x": 10
}

# extract data as a JSON string and store in text
text = json.dumps(data)

print(type(text))  # class < 'str' >
print(text) # {"x": 10}