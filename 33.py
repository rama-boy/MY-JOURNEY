data_0 = [1,2]
data_1 = [3,4]
regular_data_list = [1,2,3,4]
print(f"regular data = {regular_data_list}")

list_2D = [data_0,data_1,regular_data_list]
print(f"list 2D = {list_2D}")

# usage example
participant_0 = ["Rama",19,"Pria"]
participant_1 = ["Ikrama",20,"Pria"]
participant_2 = ["Bana",18,"Pria"]
participant_list = [participant_0,participant_1,participant_2]
print(f"participant = \n{participant_list}")
for participant in participant_list:
    print(f"NAME\t: {participant[0]}")
    print(f"AGE\t: {participant[1]}")
    print(f"GENDER\t: {participant[2]}\n")
    
# problems with references
list_copy = participant_list.copy()
print(f"participant = \n{list_copy}")
participant_0[0] = "Hydra"
print(f"participant = \n{list_copy}")
print(f"participant = \n{participant_list}")