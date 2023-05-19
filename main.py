import json

with open("sample_data.json",'r') as file:
    data = json.load(file)
    print(type(data))
    for eack_key in data:
        print(eack_key)
    new_list = []
    parameters = data["parametersList"]
    for each_parameter in parameters:
        new_dict = {
            "parameterName": each_parameter["parameterName"],
            "min_value": each_parameter["min"],
            "max_value": each_parameter["max"],
            "avg_value": each_parameter["avg"]
        }
        new_list.append(new_dict)

json_list = json.dumps(new_list, indent=4)
print(json_list)
with open("sample_out.json", "w") as file1:
    file1.write(json_list)

