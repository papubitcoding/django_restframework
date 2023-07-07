import requests
import json

URL="http://127.0.0.1:8000/st_post_api/"

headers={'content-Type': 'application/json'}

# r=requests.get(url=URL, headers=headers)

data={
  
    'name':'suresh',
    'city':'surat',
    'roll':111
}
json_data=json.dumps(data)

r=requests.post(url=URL,headers=headers,data=json_data,)
data=r.json()
print(data)

# data={
#     'id':6,
#     'name':'suresh Singh',
#     'roll':207,
#     'city':'nagpur'
# }
# json_data=json.dumps(data)

# r=requests.put(url=URL,data=json_data)
# data=r.json()
# print(data)

# data={
#     'id':4,
# }
# json_data=json.dumps(data)

# r=requests.delete(url=URL,data=json_data)
# data=r.json()
# print(data)