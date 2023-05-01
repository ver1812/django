import requests
from getpass import *
try:
    wa = "http://127.0.0.1:8000/motmsg"
    username = input("enter username ")
    password = getpass("enter password ")
    res = requests.get(wa,auth=(username,password))
    #print(res)
    data = res.json()
    #print(data)
    msg = data["msg"]
    print(msg)
except Exception as e:
    print("issue",e)