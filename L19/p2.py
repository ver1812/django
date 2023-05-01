import requests

try:
    wa = "http://127.0.0.1:8000/motmsg"
    headers ={
        "Authorization":"Token a63e2bf73d9063f1f1c8d7cf712c728346aabe45"
    }
   
    res = requests.get(wa,headers=headers)
    #print(res)
    data = res.json()
    #print(data)
    msg = data["msg"]
    print(msg)
except Exception as e:
    print("issue",e)