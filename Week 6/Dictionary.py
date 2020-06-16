# Dictionary
# A dictionary is a data structure that maps keys to values in the same way
# that a list maps indexes to values. However, keys can be any immutable value!

# stateMap = { 'pittsburgh':'PA', 'chicago':'IL', 'seattle':'WA', 'boston':'MA' }
# city = input("Enter a city name --> ").lower()
# if (city in stateMap):
#     print(city.title(), "is in", stateMap[city])
# else:
#     print("Sorry, never heard of it.")

# Create Dictionary
d = dict()
print(d)

f = { }
print(f)

pairs = [("cow", 5), ("dog", 98), ("cat", 1)]
d = dict(pairs)
print(d) # unpredictable order!

pairs = {'dog': 98, 'cow': 5}
print(pairs)

# Using Dictionary:
d = {"a": 1, "b" : 2, "c": 3}

print(len(d)) # print the number of key-value pairs

print("a" in d) # True
print(2 in d) # False, we check the keys not the values
print(2 not in d)

print(d["a"]) # Finds the value associated with the 
              #   given key. Crashes if the key is 
              #   not in d

print(d.get("z", 42)) # Finds the value of the key if 
                      #   the key is in the dict, or 
                      #   returns the second (default) 
                      #   value  if the key is not in d

d["e"] = "wow" # adds a new key-value pair to the dict
               #   or updates the value of a current key

for key in d:
    print(key, d[key]) # we can iterate over the keys, 
                       #   then print out the keys or
                       #   corresponding vlaues

# Property of Dictionary
ages = dict()
key = "fred"
value = 38
ages[key] = value
print(ages[key])

# Keys are sets
## Keys are unordered
d = dict()
d[2] = 100
d[4] = 200
d[8] = 300
print(d)  # unpredictable order
## Keys are unique
d = dict()
d[2] = 100
d[2] = 200
d[2] = 400
print(d)  # { 2:400 }
## Keys must be immutable
d = dict()
a = [1] # lists are mutable, so...
# d[a] = 42 # Error: unhashable type: 'list'
# Values are unrestricted
# values may be mutable
d = dict()
a = [1,2]
d["fred"] = a
print(d["fred"])
a += [3]
print(d["fred"]) # sees change in a!

# but keys may not be mutable
# d[a] = 42       # TypeError: unhashable type: 'list'