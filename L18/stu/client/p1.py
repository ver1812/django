import requests
while True:
    try:
        op = int(input("1.create 2.view 3.exit "))
        if op==1:
            rno = int(input("Enter rno "))
            name = input("enter name ")
            stu = {"rno":rno,"name":name}
            wa = "http://127.0.0.1:8000/stuop"
            res = requests.post(wa,stu)
            data = res.json()
            print(data)
        elif op ==2 :
            wa = "http://127.0.0.1:8000/stuop"
            res = requests.get(wa)
            data = res.json()
            print(data)
        elif op==3:
            break
        else:
            print("Invalid Input")
    except Exception as e:
        print("issue",e)
