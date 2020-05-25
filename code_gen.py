from textx import metamodel_from_file
import json


struc_meta = metamodel_from_file('ezjson/struct.tx')
test_model = struc_meta.model_from_file('create.ezjson')

main_dict = test_model.structs[0].name


# Dictionary Structure
dicts = {}
def search_temp_dict(temp_dict, targt_dict):
    try:
        if temp_dict[targt_dict] != 'null':
            result = temp_dict[targt_dict]
            del temp_dict[targt_dict]
            return result
    except:
        return targt_dict

for struct in reversed(test_model.structs):
    dicts[struct.name] = {}
    print(struct)
    for prop in struct.properties:
        dicts[struct.name][prop.name] = search_temp_dict(dicts, prop.type.name)


# Bag of Dictionaries INSERT
dicts_elems = {}
for insert in test_model.insert:
    temp_list = []
    key = insert.name.replace("I", "")
    for element in insert.propinsert:
        temp_list.append(element.name.replace("v", ""))
    dicts_elems[insert.name.replace("I", "")] = temp_list


def modify_recursive(d, bag, i):
    for k, v in d.items():
        if isinstance(v, dict):
            modify_recursive(v, bag, i)
        else:
            d[k] = bag[k][i]
    return d


# Append Final Dicts
dict_final = []

leng = 0
for item in dicts_elems.keys():
    leng = len(dicts_elems[item])

for i in range (leng):
    d = modify_recursive(dicts, dicts_elems, i)
    print(d[main_dict], '\n')
    dict_final.append(d[main_dict])

print(dict_final)


#Create JSON file
save_dir = '/Users/erik/Desktop'

json_file = json.dumps(dict_final)
with open(save_dir + '/Annotations.json', 'w') as f:
    f.write(json_file)
