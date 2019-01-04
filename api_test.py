
'''
#练习from建群
import requests
url="https://cnodejs.org/api/v1/topics"
r=requests.get(url)
r_json=r.json()
print("Status code:",r.status_code)`
print(r_json.keys())
r_json_datas=r_json["data"]
print(len(r_json_datas))
for data in r_json_datas:
    print(data)

r_json_data1=r_json_datas[0]
for key in r_json_data1.keys():
    print(key)

'''
import requests
url="http://39.107.96.138:3000/api/v1/topics"
r=requests.get(url)
r_json=r.json()
print("Status code:",r.status_code)
print(r_json.keys())
r_json_datas=r_json["data"]
print(len(r_json_datas))
for data in r_json_datas:
    print(data)
r_json_data1=r_json_datas[0]
for key in r_json_data1.keys():
    print(key)
for r_json_data in r_json_datas:
    print("\nid:",r_json_data["id"])
    print("author_id:", r_json_data["author_id"])
    print("title:", r_json_data["title"])
    print("reply_count:", r_json_data["reply_count"])
    print("author:", r_json_data["author"])


import requests
url="http://v.juhe.cn/boxoffice/rank"
r=requests.get(url)
r_json=r.json()
print("Status code:",r.status_code)
print(r_json.keys())
import virtualenv'''

print(int("10",8))
