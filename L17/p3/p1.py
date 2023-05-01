import requests

try:
    
        wa = "https://motmsg.pythonanywhere.com"
        res = requests.get(wa)
        print(res)
        data = res.json()
        print(data)
        msg = data["msg"]
        print(msg)
   
except Exception as e:
    print("issue",e)
