from django.shortcuts import render

def home(request):
    if request.GET.get("txt"):
        txt = request.GET.get("txt")
        vc , cc = 0, 0
        for t in txt:
            if t.isalpha():
                if t in "AEIOUaeiou": 
                    vc +=1
                else:
                    cc +=1

        msg = "VC = " + str(vc) + "  cc = "  + str(cc)
        return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")

