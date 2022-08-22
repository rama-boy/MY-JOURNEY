# copy dictionary

good_friends = {
    "ap":"apel",
    "pis":"pisang",
    "ang":"anggur",
    "dur":"durian",
    "mang":"mangga",
}

friends = good_friends.copy()

print(f"good_friends: {good_friends}\n")
print(f"friends: {friends}\n")

good_friends["ap"]="apel goreng"
print(f"good_friends: {good_friends}\n")
print(f"friends: {friends}\n")

# pop dictionary
dataMangga = friends.pop("mang") # by key
print(f"data mangga = {dataMangga}\n")
print(f"friends = {friends}\n")

# popitem dictionary
dataTerakhir = friends.popitem() # based on the latest data
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")

