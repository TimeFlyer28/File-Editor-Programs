
# Write Dicitonary

thisdict = {
  "brand": "Tesla",
  "model": "X",
  "year": 2019
}


with open('text.txt', 'w') as f:
    f.write(str(thisdict))