my_friends = {
    "ikr":"IKRAMA",
    "hds":"HADES",
    "ath":"ATHENA",
    "zs":"ZEUS",
    "psd":"POSEIDON"
}

# looping first try (what comes out is the key)
for friends in my_friends:
    print(friends)
    
# operator to pick up items / iterables
keys = my_friends.keys()
print(keys)
for key in my_friends.keys():
    print(my_friends.get(key))

values = my_friends.values()
print(values)
for value in my_friends.values():
    print(value)
    
items = my_friends.items()
print(items)
for item in my_friends.items():
    print(item)

for key,value in my_friends.items():
    print(f"key = {key}, value = {value}")