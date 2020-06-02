from textx import metamodel_from_file
import json
import copy

struc_meta = metamodel_from_file('tx_ezjson/ezjson.tx')
test_model = struc_meta.model_from_file('create.ezjson')

for struct in test_model.structs:
    print(struct)
    for prop in struct.properties:
        print(prop.name)

print('\n')
# Bag of Dictionaries INSERT
for insert in test_model.insert:
    print(insert)
    for element in insert.propinsert:
        print(element)
        