# Operation Dictionary

data_dict = {
    "rm":"rama",
    "bn":"bana",
    "ikr":"ikrama",
}

# dictionary length
LENDICT = len(data_dict)
print(f"dictionary length : {LENDICT}")

# check whether the key exists or not
KEY = "rm"
CHECKKEY = KEY in data_dict
print(f"is the {KEY} in data_dict : {CHECKKEY}")

# access value (read) with get
print(data_dict["rm"])
print(data_dict.get("rm"))
print(data_dict.get("RM","KEY NOT FOUND!")) # check key with message : KEY NOT FOUND!

# Updating data
data_dict["rm"] = "RAMARAMARAMA"
print(data_dict)
data_dict["kr"] = "Kings Rama"
print(data_dict)

data_dict.update({"rm":"rama"})
print(data_dict)
data_dict.update({"ath":"Goddess Athena"}) # if for example there is no data, it will be added automatically
print(data_dict)

# delete data on dict
del data_dict["ath"]
print(data_dict)