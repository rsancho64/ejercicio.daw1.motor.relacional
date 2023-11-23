# STUDIO:
# 
# https://www.w3schools.com/python/python_json.asp

# - [ ] try a complex json like this ...
# 1	{
# 2	    "firstName": "John",
# 3	    "lastName": "Smith",
# 4	    "address": {
# 5	        "streetAddress": "21 2nd Street",
# 6	        "city": "New York",
# 7	        "state": "NY",
# 8	        "postalCode": 10021
# 9	    },
# 10	    "phoneNumbers": [
# 11	        "212-732-1234",
# 12	        "646-123-4567"
# 13	    ]
# 14	}
# ... from https://www.ibm.com/docs/es/baw/20.x?topic=formats-javascript-object-notation-json-format

import json

# rows = [
#     {'nombre': 'marta', 'edad': 22, 'jefe': 'andres'},
#     {'nombre': 'andres', 'edad': 32, 'jefe': 'juan'},
#     {'nombre': 'diego', 'edad': 33, 'jefe': 'juan'},
#     {'nombre': 'juan', 'edad': 45, 'jefe': None}
# ]
# print('DATA:\n', repr(rows))

# rows.append({'nombre': 'farala', 'edad': 25, 'jefe': 'juan'})
# print('JSON:\n', json.dumps(rows))

# some JSON:
s = '{"name": "John", "age": 30}'
d = {"name": "John", "age": 30}
print(type(s))
print(type(d))

# JSON?
ss = '{{"name": "John", "age": 30}, {"name": "Ava", "age": 20}}'
dd = [{"name": "John", "age": 30},{"name": "John", "age": 30}]
print(type(ss))
print(type(dd))

# parse x:
s_js = json.loads(s)
ss_js = json.loads(ss)

# the result is a Python dictionary:
# print(js["age"])

