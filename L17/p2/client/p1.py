import requests
while True:
    try:
        op = int(input("1.date 2.time 3.date and time 4.exit "))
        if op ==1:
            wa = "http://127.0.0.1:8000/dt"
            res = requests.get(wa)
            data = res.json()
            msg = data["msg"]
            print(msg)
        elif op ==2:
            wa = "http://127.0.0.1:8000/ti"
            res = requests.get(wa)
            data = res.json()
            msg = data["msg"]
            print(msg)
        elif op ==3:
            wa = "http://127.0.0.1:8000/dtti"
            res = requests.get(wa)
            data = res.json()
            msg = data["msg"]
            print(msg)
        elif op==4:
            break
        else:
            print("Sorry Invalid")
    except Exception as e:
        print("issue",e)
