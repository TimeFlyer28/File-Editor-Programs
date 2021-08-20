
# Read Dictionary

import ast


urmom = {
  "brand": "Rover",
  "model": "3",
  "year": 21
}

print (urmom)
print (urmom['brand'])

with open('text.txt', 'r') as f:
    urmom = ast.literal_eval(f.read())


print (urmom)
print (urmom['brand'])