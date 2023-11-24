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

