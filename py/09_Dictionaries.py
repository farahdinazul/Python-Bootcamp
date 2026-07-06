# employee  = {
#     "name" : "Farah",
#     "age" : "43",
#     "department" : "HR",
#     "PPA 3 years" : ["2", "3", "3"]
# }

# print(employee["name"]) #Farah
# print(employee.get("age")) #43
# employee["age"] = 44
# employee["email"] = "farahdinazul@company.com"
# print(employee.get("age")) #44

# keys = employee.keys() #getallkeys
# values = employee.values() #getallvalues
# items = employee.items() #getboth key and values

# print(keys)
# print(items)
# print(values)

# for key, value in employee.items():
#     print(f"{key}:{value}")

#nested dictionaries
company = {
    "employees":{
        "Farah" : {"jobgrade": "Manager", "department": "Commercial"},
        "Yasmin" : {"jobgrade": "Executive", "department": "HR"}
    },
    "departments": ["Commercial", "HR", "IT"]
}   

print(company["employees"].items())
print(company["departments"])